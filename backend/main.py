from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.chat import router as chat_router
from contextlib import asynccontextmanager

# 导入 LLM 客户端的初始化/关闭函数
from service.llm_service import init_llm_client, close_llm_client


# 新版生命周期
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时执行
    await init_llm_client()
    print("✅ AI 大模型客户端已启动！")
    yield  # 服务运行中
    # 关闭时执行
    await close_llm_client()
    print("✅ AI 客户端已安全关闭！")

# 创建后端服务 配置生命周期
app = FastAPI(title="AI 助手", lifespan=lifespan)

# 跨域配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由 挂载路由
app.include_router(chat_router)

# 测试首页
@app.get("/")
def home():
    return {"message": "AI 助手后端已启动"}

if __name__ == "__main__":
    import uvicorn
    from core.settings import settings
    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=True
    )

