from fastapi import FastAPI
# Import the router from health.py
from enterprise_ai.api.routes.health import router as health_router
from enterprise_ai.api.routes.upload import router as upload_router
app = FastAPI(
    title="Enterprise AI Engineering Assistant",
    version="0.1.0",
    description="Enterprise Agentic Hybrid RAG Platform",
)

# Register the health router
app.include_router(health_router)
app.include_router(upload_router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Enterprise AI Engineering Assistant"
    }
