from openai import AsyncOpenAI
from core.settings import settings

# 全局 client（先不创建）
client = None


# ==========================================
# 【生命周期用】启动时创建连接
# ==========================================
async def init_llm_client():
    global client
    client = AsyncOpenAI(
        api_key=settings.OPENAI_API_KEY,
        base_url=settings.OPENAI_BASE_URL
    )


# ==========================================
# 【生命周期用】关闭时释放连接
# ==========================================
async def close_llm_client():
    global client
    if client:
        await client.http_client.aclose()  # ✅ 手动关闭底层的 HTTP 连接池
        client = None


# ==========================================
# 你的AI调用函数
# ==========================================
async def chat_with_llm(prompt: str):
    if client is None:
        raise RuntimeError("LLM 客户端未初始化，请先调用 init_llm_client()")
    response = await client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {"role": "system", "content": """
你是一个友好的中文AI助手。
回答规则：
1. 使用 **加粗** 突出重点
2. 分点用 - 列表
3. 段落之间换行
4. 重要标题用 ### 开头
5. 全程用中文，清晰易读
"""},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
