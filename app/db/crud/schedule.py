from app.db.database import get_schedule_collection
from pymongo.results import InsertOneResult, InsertManyResult
from typing import List, Dict, Any, Optional

from app.schemas.schedule import LessonAddSchema
from app.services.schedule import fetch_and_form_schedule


async def add_schedule_group(lessons: List[LessonAddSchema]) -> InsertManyResult:
    ...

async def add_lesson(lesson: LessonAddSchema, collection) -> InsertOneResult:
    filter = {
        'discipline': lesson['discipline'],
        'date': lesson['date'],
        'time_begin': lesson['time_begin'],
        'group_id': lesson['group_id']
    }
    result = await collection.update_one(
        filter,
        {'$set': lesson},
        upsert=True
    )
    print(f"[DB] {result}")
    return result


async def add_schedule(schedule_data: Dict[str, Any], group_id: str, collection):
    for cur_date, lessons in schedule_data.items():
        for lesson in lessons:
            lesson['group_id'] = group_id
            result = await add_lesson(lesson, collection)
            print(result)
