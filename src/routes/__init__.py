from fastapi import APIRouter
from .ai import router as ai_router
from .auth import router as auth_router
from .citizen_reports import router as citizen_reports_router

router = APIRouter()
router.include_router(ai_router)
router.include_router(auth_router)
router.include_router(citizen_reports_router)