
from fastapi import HTTPException
from fastapi import APIRouter
from typing import Dict
from app.services.schedule import get_group_id

router = APIRouter()


@router.get("/groups/id/{group_name}")
async def get_group_id_by_name(group_name: str):
    response = await get_group_id(group_name)
    if response['message'] == "ok":
        return response
    raise HTTPException(302, response['data'])




