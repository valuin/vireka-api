from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os
import json
import psycopg2
from psycopg2.extras import Json
from typing import List, Optional
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/ai", tags=["AI"])

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Add this function if not already imported from your main file
def get_db_connection():
    load_dotenv()
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

# Request models
class ChatRequest(BaseModel):
    message: str
    context: Optional[str] = None

class RiskAssessmentRequest(BaseModel):
    environmental_data: List[dict]

# Disease-focused response models
class DiseaseData(BaseModel):
    name: str
    percentage: float  # 0-1 range
    riskLevel: str  # "low", "medium", "high"
    explanationWhyItsFeasible: str
    prevention: List[str]  # Array of prevention recommendations

class RiskAssessmentResponse(BaseModel):
    diseaseData: List[DiseaseData]
    overview: str

# Keep existing chat models
class RiskLevel(BaseModel):
    level: str  # "Low", "Moderate", "High", "Critical"
    confidence: float
    factors: List[str]

class ActionablePlan(BaseModel):
    title: str
    description: str
    priority: str
    estimated_impact: str

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

@router.post("/risk-assessment", response_model=List[RiskAssessmentResponse])
async def assess_environmental_risk(request: RiskAssessmentRequest):
    """Assess disease risks based on environmental data for multiple locations"""
    try:
        responses = []
        
        for env_data in request.environmental_data:
            location = env_data.get('province', 'Unknown Location')
            
            print(f"Analyzing data for: {location}")
            print(f"Environmental data: {env_data}")
            
            prompt = f"""
            Analyze disease risk potential for kelurahan: {location}
            Environmental data: {env_data}
            
            Based on the environmental indicators provided, assess potential disease risks:
            
            Key environmental factors to consider:
            - Air Quality Index (AQI): {env_data.get('aqi', 'N/A')}
            - PM2.5 levels: {env_data.get('pm25', 'N/A')} μg/m³
            - NO2 levels: {env_data.get('no2', 'N/A')} μg/m³
            - CO levels: {env_data.get('co', 'N/A')} mg/m³
            - SO2 levels: {env_data.get('so2', 'N/A')} μg/m³
            - O3 levels: {env_data.get('o3', 'N/A')} mg/m³
            - NDVI (vegetation): {env_data.get('ndvi', 'N/A')}
            - Precipitation: {env_data.get('precipitation', 'N/A')} mm
            - Poverty index: {env_data.get('poverty_index', 'N/A')}
            
            IMPORTANT: You must return a JSON response with exactly this structure:
            {{
                "diseaseData": [
                    {{
                        "name": "Disease Name",
                        "percentage": 0.5,
                        "riskLevel": "high",
                        "explanationWhyItsFeasible": "Explanation of why this disease is likely",
                        "prevention": "Prevention recommendations"
                    }}
                ],
                "overview": "Overall health risk assessment explanation"
            }}
            
            Guidelines for assessment:
            - If AQI > 100 OR PM2.5 > 35: Include respiratory diseases (ISPA, Asma)
            - If high precipitation + low NDVI: Include vector-borne diseases (DBD, Malaria)
            - If high poverty index: Increase vulnerability scores
            - If NO2/SO2 high: Include respiratory irritation risks
            
            Risk levels: "low", "medium", "high"
            Percentage should be between 0.0 and 1.0
            
            If environmental conditions are relatively safe (AQI < 50, PM2.5 < 15, good NDVI):
            - Return empty diseaseData array: []
            - Explain in overview why the area is considered environmentally safe
            
            Focus on Indonesian common diseases: ISPA, DBD, Diare, Malaria, Asma, Pneumonia
            
            output should be in Indonesian.
            """
            
            response = client.responses.parse(
                model="gpt-4o-mini",
                input=[
                    {
                        "role": "system", 
                        "content": """You are an expert environmental health analyst specializing in Indonesian public health. 
                        Analyze environmental data to predict disease risks for kelurahan areas in Indonesia.
                        
                        Focus on:
                        - Air quality impacts: ISPA, Asma, Pneumonia
                        - Vector-borne diseases: DBD (Dengue), Malaria, Chikungunya  
                        - Water-related diseases: Diare, Tifus
                        - Environmental factors: AQI, PM2.5, precipitation, NDVI, poverty index
                        
                        Use WHO and Indonesian Ministry of Health standards for risk thresholds.
                        Always return valid JSON with diseaseData array and overview string.
                        Be specific about Indonesian disease names and prevention methods.
                        output should be in Indonesian."""
                    },
                    {"role": "user", "content": prompt}
                ],
                text_format=RiskAssessmentResponse,
            )
            
            # Save the results to database
            try:
                conn = get_db_connection()
                cur = conn.cursor()
                
                # Convert complete output to dictionary and then to JSON
                complete_output = {
                    "diseaseData": [disease.dict() for disease in response.output_parsed.diseaseData],
                    "overview": response.output_parsed.overview
                }
                complete_json = json.dumps(complete_output)
                
                # Update query to set diseases column
                query = """
                    UPDATE infrastructure 
                    SET diseases = %s::jsonb 
                    WHERE province = %s
                """
                
                cur.execute(query, (complete_json, location))
                conn.commit()
                
                print(f"Successfully saved risk assessment data for {location}")
                
            except Exception as db_error:
                print(f"Error saving to database for {location}: {str(db_error)}")
                # Continue with the response even if database save fails
            
            responses.append(response.output_parsed)
        
        return responses
        
    except Exception as e:
        print(f"Error in risk assessment: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Disease risk assessment failed: {str(e)}")

@router.get("/health")
async def health_check():
    """Health check for AI service"""
    return {"status": "healthy", "service": "ai", "model": "gpt-4o-mini"}