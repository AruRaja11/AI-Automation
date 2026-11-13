from fastapi import APIRouter
import os 


router = APIRouter(
    prefix="/health",
    tags=['Health']
)

@router.get("/")
async def get_health():
    return {
        "status": "success",
        "message": "successfully connected"
    }

