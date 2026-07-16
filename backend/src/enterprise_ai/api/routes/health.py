from fastapi import APIRouter

# Initialize the router
router = APIRouter(
    tags=["Health"]
)

@router.get("/health")
async def health_check():
    return {"status": "healthy"}
