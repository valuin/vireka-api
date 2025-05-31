from fastapi import APIRouter, HTTPException, Depends, Query
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
import json
from .auth import get_supabase_client
from supabase import Client

router = APIRouter(prefix="/citizen-reports", tags=["Citizen Reports"])

class CitizenReportCreate(BaseModel):
    whatsapp_user_id: str = Field(..., max_length=255)
    report_type: str
    description: str
    kecamatan: Optional[str] = None
    kelurahan: Optional[str] = None
    puskesmas_id: Optional[str] = None

class CitizenReportUpdate(BaseModel):
    report_status: Optional[str] = None
    llm_processed_output: Optional[dict] = None

class CitizenReportResponse(BaseModel):
    id: str
    whatsapp_user_id: str
    report_type: str
    description: str
    kecamatan: Optional[str]
    kelurahan: Optional[str]
    report_status: str
    reported_at: str
    puskesmas_id: Optional[str]
    llm_processed_output: Optional[dict]

@router.post("/", response_model=CitizenReportResponse)
async def create_citizen_report(
    report: CitizenReportCreate,
    supabase: Client = Depends(get_supabase_client)
):
    """
    ## Create New Citizen Report
    
    Submit a new citizen report for environmental or health issues.
    
    **Report Types**: Environmental pollution, health symptoms, water quality, air quality, etc.
    """
    report_data = {
        "whatsapp_user_id": report.whatsapp_user_id,
        "report_type": report.report_type,
        "description": report.description,
        "kecamatan": report.kecamatan,
        "kelurahan": report.kelurahan,
        "puskesmas_id": report.puskesmas_id,
        "report_status": "pending"
    }
    
    response = supabase.table("citizen_reports").insert(report_data).execute()
    
    if not response.data:
        raise HTTPException(status_code=500, detail="Failed to create citizen report")
    
    created_report = response.data[0]
    return CitizenReportResponse(**created_report)

@router.get("/", response_model=List[CitizenReportResponse])
async def get_citizen_reports(
    status: Optional[str] = Query(None, description="Filter by report status"),
    report_type: Optional[str] = Query(None, description="Filter by report type"),
    kecamatan: Optional[str] = Query(None, description="Filter by kecamatan"),
    limit: int = Query(50, ge=1, le=100, description="Number of reports to return"),
    offset: int = Query(0, ge=0, description="Number of reports to skip"),
    supabase: Client = Depends(get_supabase_client)
):
    """
    ## Get Citizen Reports
    
    Retrieve citizen reports with optional filtering.
    """
    query = supabase.table("citizen_reports").select("*")
    
    # Apply optional filters
    if status:
        valid_statuses = ["pending", "reviewed", "in_progress", "resolved", "invalid"]
        if status not in valid_statuses:
            raise HTTPException(status_code=400, detail=f"Invalid status. Must be one of: {valid_statuses}")
        query = query.eq("report_status", status)
    
    if report_type:
        query = query.eq("report_type", report_type)
    
    if kecamatan:
        query = query.eq("kecamatan", kecamatan)
    
    # Apply pagination
    query = query.range(offset, offset + limit - 1).order("reported_at", desc=True)
    
    response = query.execute()
    
    if not response.data:
        return []
    
    return [CitizenReportResponse(**report) for report in response.data]

@router.get("/{report_id}", response_model=CitizenReportResponse)
async def get_citizen_report(
    report_id: str,
    supabase: Client = Depends(get_supabase_client)
):
    """
    ## Get Single Citizen Report
    
    Retrieve a specific citizen report by ID.
    """
    response = supabase.table("citizen_reports").select("*").eq("id", report_id).execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Citizen report not found")
    
    report = response.data[0]
    return CitizenReportResponse(**report)

@router.patch("/{report_id}", response_model=CitizenReportResponse)
async def update_citizen_report(
    report_id: str,
    update_data: CitizenReportUpdate,
    supabase: Client = Depends(get_supabase_client)
):
    """
    ## Update Citizen Report
    
    Update report status or add LLM processing results.
    """
    # Check if report exists
    response = supabase.table("citizen_reports").select("*").eq("id", report_id).execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Citizen report not found")
    
    # Prepare update data
    update_dict = {}
    if update_data.report_status:
        valid_statuses = ["pending", "reviewed", "in_progress", "resolved", "invalid"]
        if update_data.report_status not in valid_statuses:
            raise HTTPException(status_code=400, detail=f"Invalid status. Must be one of: {valid_statuses}")
        update_dict["report_status"] = update_data.report_status
    
    if update_data.llm_processed_output:
        update_dict["llm_processed_output"] = update_data.llm_processed_output
    
    if not update_dict:
        raise HTTPException(status_code=400, detail="No valid fields to update")
    
    # Update the report
    response = supabase.table("citizen_reports").update(update_dict).eq("id", report_id).execute()
    
    if not response.data:
        raise HTTPException(status_code=500, detail="Failed to update citizen report")
    
    return CitizenReportResponse(**response.data[0])

@router.delete("/{report_id}")
async def delete_citizen_report(
    report_id: str,
    supabase: Client = Depends(get_supabase_client)
):
    """
    ## Delete Citizen Report
    
    Delete a citizen report.
    """
    # Check if report exists
    response = supabase.table("citizen_reports").select("*").eq("id", report_id).execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Citizen report not found")
    
    # Delete the report
    response = supabase.table("citizen_reports").delete().eq("id", report_id).execute()
    
    return {"message": "Citizen report deleted successfully"}

@router.get("/stats/summary")
async def get_reports_summary(
    supabase: Client = Depends(get_supabase_client)
):
    """
    ## Get Reports Summary Statistics
    
    Get summary statistics for citizen reports.
    
    **Returns**: Count by status, type, and recent activity
    """
    response = supabase.table("citizen_reports").select("report_status, report_type, reported_at").execute()
    
    if not response.data:
        return {
            "total_reports": 0,
            "status_breakdown": {},
            "type_breakdown": {},
            "recent_reports": 0
        }
    
    reports = response.data
    
    # Calculate statistics
    status_breakdown = {}
    type_breakdown = {}
    recent_reports = 0
    current_time = datetime.now()
    
    for report in reports:
        # Status breakdown
        status = report.get("report_status", "pending")
        status_breakdown[status] = status_breakdown.get(status, 0) + 1
        
        # Type breakdown
        report_type = report.get("report_type", "unknown")
        type_breakdown[report_type] = type_breakdown.get(report_type, 0) + 1
        
        # Recent reports (last 7 days)
        if report.get("reported_at"):
            reported_time = datetime.fromisoformat(report["reported_at"].replace("Z", "+00:00"))
            if (current_time - reported_time).days <= 7:
                recent_reports += 1
    
    return {
        "total_reports": len(reports),
        "status_breakdown": status_breakdown,
        "type_breakdown": type_breakdown,
        "recent_reports": recent_reports
    }

@router.get("/health")
async def reports_health_check():
    """Health check for citizen reports service"""
    return {"status": "healthy", "service": "citizen-reports"}
