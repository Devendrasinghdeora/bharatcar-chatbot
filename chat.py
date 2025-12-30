from fastapi import APIRouter
from chatapp.controllers.chat_controller import chat_handler
from chatapp.schemas.chat_schema import ChatRequest

router = APIRouter()

@router.post("/")
def chat(payload: ChatRequest):
    return chat_handler(payload.dict())
