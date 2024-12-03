from fastapi import APIRouter

from app.db.crud.group import add_group
from app.schemas.group import GroupModel

router = APIRouter()

@router.post("/add_group")
async def add_group_to_db(model: GroupModel):
    try:
        response = await add_group(model)
        return {"message": "OK",
                "data": None,
                "isUpdated": response.raw_result.get("updatedExisting", False)}
    except Exception as e:
        return {"message": f"NOT OK",
                'exception': str(e)}