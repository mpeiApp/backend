from fastapi import HTTPException, Depends, APIRouter
from typing import Dict, Union
from app.services.schedule import get_group_id, get_schedule, form_schedule, fetch_and_form_schedule
from app.schemas.schedule import GroupIDResponseSchema, ScheduleResponseSchema, ScheduleRequestSchema
from app.db.crud.schedule import add_schedule, get_week_schedule

router = APIRouter()


@router.get("/groups/id", response_model=GroupIDResponseSchema)
async def get_group_id_by_name(group_name: str):
    response = await get_group_id(group_name)
    if response['message'] == "ok":
        return response
    raise HTTPException(status_code=302, detail=response['data'])


@router.get("/by_id", response_model=ScheduleResponseSchema)
async def get_schedule_by_group_id(request: ScheduleRequestSchema = Depends()):
    schedule_response = await fetch_and_form_schedule(request.group_id, request.date_start, request.date_end)
    return ScheduleResponseSchema(message=schedule_response['message'], data=schedule_response['data'])


@router.post("/by_timestamp")
async def get_schedule_by_timespan(group_id: str, start_date: str, end_date: str):
    response = await get_week_schedule(group_id, start_date, end_date)
    result = {}
    for el in response:
        el['_id'] = str(el['_id'])
        if el['date'] in result:
            result[el['date']].append(el)
        else:
            result[el['date']] = [el]
    return result
