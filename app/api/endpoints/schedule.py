from fastapi import HTTPException, Depends, APIRouter
from typing import Dict, Union
from app.services.schedule import get_group_id, get_schedule, form_schedule, fetch_and_form_schedule
from app.schemas.schedule import GroupIDResponseSchema, ScheduleResponseSchema, ScheduleRequestModel

router = APIRouter()


@router.get("/groups/id", response_model=GroupIDResponseSchema)
async def get_group_id_by_name(group_name: str):
    response = await get_group_id(group_name)
    if response['message'] == "ok":
        return response
    raise HTTPException(status_code=302, detail=response['data'])


@router.get("/by_id", response_model=ScheduleResponseSchema)
async def get_schedule_by_group_id(request: ScheduleRequestModel = Depends()):
    schedule_response = await fetch_and_form_schedule(request.group_id, request.date_start, request.date_end)
    return ScheduleResponseSchema(message=schedule_response['message'], data=schedule_response['data'])






