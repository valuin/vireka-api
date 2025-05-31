from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel, EmailStr
from supabase import Client
from typing import Optional
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/auth", tags=["Authentication"])

def get_supabase_client() -> Client:
    from supabase import create_client
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
    return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

class SignUpRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "citizen"  # default role
    phone: Optional[int] = None
    puskesmas_id: Optional[str] = None

class SignInRequest(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    email: str
    role: str
    puskesmas_id: Optional[str] = None
    created_at: str

class AuthResponse(BaseModel):
    user: UserResponse
    access_token: str
    refresh_token: str

@router.post("/sign-up", response_model=AuthResponse)
async def sign_up(request: SignUpRequest, supabase: Client = Depends(get_supabase_client)):
    """Sign up a new user with Supabase Auth and insert into users table"""
    try:
        # Validate role
        valid_roles = ["staff", "admin", "citizen"]
        if request.role not in valid_roles:
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid role. Must be one of: {', '.join(valid_roles)}"
            )
        
        # Create user with Supabase Auth
        auth_response = supabase.auth.sign_up({
            "email": request.email,
            "password": request.password
        })
        
        if not auth_response.user:
            raise HTTPException(status_code=400, detail="Failed to create user account")
        
        # Hash password for storage in users table
        password_hash = hashlib.sha256(request.password.encode()).hexdigest()
        
        # Insert user data into custom users table
        user_data = {
            "id": auth_response.user.id,
            "email": request.email,
            "name": request.name,
            "phone": request.phone,
            "password_hash": password_hash,
            "role": request.role,
            "puskesmas_id": request.puskesmas_id
        }
        
        db_response = supabase.table("users").insert(user_data).execute()
        
        if not db_response.data:
            # If user table insert fails, we should clean up the auth user
            try:
                supabase.auth.admin.delete_user(auth_response.user.id)
            except:
                pass  # Continue even if cleanup fails
            raise HTTPException(status_code=500, detail="Failed to create user profile")
        
        user_profile = db_response.data[0]
        
        return AuthResponse(
            user=UserResponse(
                id=user_profile["id"],
                email=user_profile["email"],
                role=user_profile["role"],
                puskesmas_id=user_profile["puskesmas_id"],
                created_at=user_profile["created_at"]
            ),
            access_token=auth_response.session.access_token if auth_response.session else "",
            refresh_token=auth_response.session.refresh_token if auth_response.session else ""
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Sign up failed: {str(e)}")

@router.post("/sign-in", response_model=AuthResponse)
async def sign_in(request: SignInRequest, supabase: Client = Depends(get_supabase_client)):
    """Sign in user with Supabase Auth and return user profile"""
    try:
        # Authenticate with Supabase Auth
        auth_response = supabase.auth.sign_in_with_password({
            "email": request.email,
            "password": request.password
        })
        
        if not auth_response.user:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        
        # Get user profile from users table
        user_response = supabase.table("users").select("*").eq("id", auth_response.user.id).execute()
        
        if not user_response.data:
            raise HTTPException(status_code=404, detail="User profile not found")
        
        user_profile = user_response.data[0]
        
        return AuthResponse(
            user=UserResponse(
                id=user_profile["id"],
                email=user_profile["email"],
                role=user_profile["role"],
                puskesmas_id=user_profile["puskesmas_id"],
                created_at=user_profile["created_at"]
            ),
            access_token=auth_response.session.access_token if auth_response.session else "",
            refresh_token=auth_response.session.refresh_token if auth_response.session else ""
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Sign in failed: {str(e)}")

@router.post("/sign-out")
async def sign_out(supabase: Client = Depends(get_supabase_client)):
    """Sign out current user"""
    try:
        supabase.auth.sign_out()
        return {"message": "Successfully signed out"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Sign out failed: {str(e)}")

async def get_current_user_from_token(
    authorization: Optional[str] = Header(None),
    supabase: Client = Depends(get_supabase_client)
) -> UserResponse:
    """Dependency to get current authenticated user from Authorization header"""
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid authorization header")
    
    token = authorization.replace("Bearer ", "")
    
    # Get user from Supabase using the JWT token
    user_response = supabase.auth.get_user(token)
    
    if not user_response or not user_response.user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    # Get user profile from users table
    profile_response = supabase.table("users").select("*").eq("id", user_response.user.id).execute()
    
    if not profile_response.data:
        raise HTTPException(status_code=404, detail="User profile not found")
    
    user_profile = profile_response.data[0]
    
    return UserResponse(
        id=user_profile["id"],
        email=user_profile["email"],
        role=user_profile["role"],
        puskesmas_id=user_profile["puskesmas_id"],
        created_at=user_profile["created_at"]
    )

@router.get("/me", response_model=UserResponse)
async def get_current_user(current_user: UserResponse = Depends(get_current_user_from_token)):
    """Get current authenticated user profile"""
    return current_user

@router.get("/health")
async def auth_health_check():
    """Health check for auth service"""
    return {"status": "healthy", "service": "auth"}
