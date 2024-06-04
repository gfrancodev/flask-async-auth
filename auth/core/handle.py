from os import getenv
import uvicorn

async def handle():
    PORT = int(getenv("PORT", 5000))
    server = uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=PORT,
        use_colors=True,
        reload=True,
        reload_includes=["*.py"],
    )
    await server