from fastapi import APIRouter
from services.AIServiceLayer import AIServices

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)

services = AIServices()

@router.post("")
async def ai_chat(request:str):
    try:
        return services.ai_response(request)

    except Exception as e:
        return {
            "status": "failed",
            "message": "something went wrong"
        }