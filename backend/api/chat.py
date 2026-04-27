from fastapi import APIRouter
from pydantic import BaseModel
from service.llm_service import chat_with_llm

# 👇 在这里导入统一响应工具
from utils.response import success_response, error_response

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str

@router.post("/chat")
async def chat(req: ChatRequest):
    try:
        reply = await chat_with_llm(req.prompt)
        # ✅ 成功：用标准格式返回
        return success_response(reply)
    except Exception as e:
        # ✅ 失败：用标准错误格式返回
        return error_response(f"AI 服务异常：{str(e)}")

