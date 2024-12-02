from fastapi import APIRouter
from app.services.login import login_to_bars
from app.schemas.user import UserModel

router = APIRouter()

@router.post("/login")
async def root(model: UserModel):
    try:
        result = await login_to_bars(model.username, model.password)
        # return result
        return {
            "message": "OK",
            "data": result
        }
    except Exception as e:
        # return {"error": str(e)}
        return {
            "message": f"NOT OK",
            "data": str(e)
        }