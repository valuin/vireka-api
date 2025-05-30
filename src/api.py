import os
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL: str = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY: str = os.getenv("SUPABASE_ANON_KEY")

if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    raise ValueError("SUPABASE_URL and SUPABASE_ANON_KEY must be set in the .env file")

def get_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

app = FastAPI()

class Test(BaseModel):
    id: str | None = None 
    text: str | None = None
    created_at: str | None = None

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI with Supabase!"}

@app.get("/test", response_model=list[Test])
def read_test_data(supabase: Client = Depends(get_supabase_client)):
    try:
        data, count = supabase.table("test").select("*").execute()
        print(f"Retrieved {count} records from 'test' table")
        if not data or not data[1]:
            return []
        return [Test(**item) for item in data[1]]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Supabase error: {e}")

@app.post("/add-test/", response_model=Test)
def create_item(item: Test, supabase: Client = Depends(get_supabase_client)):
    try:
        data, count = supabase.table("test").insert(item.model_dump(exclude_unset=True)).execute()
        if not data:
            raise HTTPException(status_code=500, detail="Failed to create item in Supabase")
        return Test(**data[1][0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Supabase error: {e}")