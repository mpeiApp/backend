import asyncio
import os
from datetime import datetime

from app.db.crud.schedule import add_lesson, add_schedule
from app.db.database import database, get_schedule_collection
from app.services.schedule import fetch_and_form_schedule

TIME_PARSE_SCHEDULE = int(os.getenv("TIME_PARSE_SCHEDULE", 6))

GROUP_LIST = [18032,18042]

async def schedule_job():
    collection = await get_schedule_collection()
    try:
        for group_id in GROUP_LIST:
            response = await fetch_and_form_schedule(group_id, '2024-11-11', '2024-11-15')
            if response['message'] == 'ok':
                data = response['data']
                result = await add_schedule(data, str(group_id), collection)
                print(result)
            print('-'*10)
    except Exception as e:
        print(f"[ERROR] {e}")


# def schedule_job_wrapper():
#     await schedule_job()

