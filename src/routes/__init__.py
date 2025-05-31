from fastapi import APIRouter
from .ai import router as ai_router

router = APIRouter(prefix="/api")
router.include_router(ai_router)