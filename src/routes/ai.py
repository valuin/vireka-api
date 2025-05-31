from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os
from typing import List, Optional

router = APIRouter(prefix="/ai", tags=["AI"])

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Request models
class ChatRequest(BaseModel):
    message: str
    context: Optional[str] = None

class RiskAssessmentRequest(BaseModel):
    location: str
    environmental_data: dict

# Structured output models
class RiskLevel(BaseModel):
    level: str  # "Low", "Moderate", "High", "Critical"
    confidence: float
    factors: List[str]

class ActionablePlan(BaseModel):
    title: str
    description: str
    priority: str
    estimated_impact: str

class RiskAssessmentResponse(BaseModel):
    risk_level: RiskLevel
    actionable_plans: List[ActionablePlan]
    summary: str

class ChatResponse(BaseModel):
    response: str
    suggestions: List[str]

@router.post("/chat", response_model=ChatResponse)
async def chat_with_ai(request: ChatRequest):
    """General chat endpoint with structured response"""
    try:
        messages = [
            {"role": "system", "content": "You are Vireka AI, an environmental risk assessment assistant. Provide helpful, accurate information about environmental hazards and safety measures."},
            {"role": "user", "content": request.message}
        ]
        
        if request.context:
            messages.insert(1, {"role": "user", "content": f"Context: {request.context}"})
        
        response = client.responses.parse(
            model="gpt-4o-mini",
            input=messages,
            text_format=ChatResponse,
        )
        
        return response.output_parsed
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI processing failed: {str(e)}")

@router.post("/risk-assessment", response_model=RiskAssessmentResponse)
async def assess_environmental_risk(request: RiskAssessmentRequest):
    """Assess environmental risks with structured output"""
    try:
        prompt = f"""
        Analyze environmental risk for location: {request.location}
        Environmental data: {request.environmental_data}
        
        Provide a comprehensive risk assessment including:
        1. Overall risk level (Low/Moderate/High/Critical) with confidence score
        2. Contributing factors that led to this assessment
        3. Actionable safety plans with priorities and estimated impact
        4. Summary of findings
        """
        
        response = client.responses.parse(
            model="gpt-4o-mini",
            input=[
                {"role": "system", "content": "You are an expert environmental risk analyst. Analyze data and provide structured risk assessments with specific focus on air quality, flood risks, disease outbreaks, and weather patterns."},
                {"role": "user", "content": prompt}
            ],
            text_format=RiskAssessmentResponse,
        )
        
        return response.output_parsed
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Risk assessment failed: {str(e)}")

@router.get("/health")
async def health_check():
    """Health check for AI service"""
    return {"status": "healthy", "service": "ai", "model": "gpt-4o-2024-08-06"}
