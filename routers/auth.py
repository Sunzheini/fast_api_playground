from fastapi import APIRouter

router = APIRouter()


# http://127.0.0.1:8000/auth
@router.get("/auth/")
async def get_user():
    return {"user": "authenticated"}
