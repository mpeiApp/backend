from typing import Dict, Any
from pymongo.results import InsertOneResult
from app.db.database import get_grades_collection
from pymongo.results import UpdateResult

from app.schemas.user import PersonGradesInfo


async def add_person_grades(grade_data: PersonGradesInfo) -> UpdateResult:
    collection = await get_grades_collection()

    # Преобразуем объект в словарь
    grade_data_dict = grade_data.dict()

    # Условие фильтрации для обновления
    filter_condition = {
        "studentInfo.login": grade_data.studentInfo.login,
        "studentInfo.name": grade_data.studentInfo.name,
        "studentInfo.surname": grade_data.studentInfo.surname,
        "studentInfo.groupNumber": grade_data.studentInfo.groupNumber
    }

    # Выполняем обновление или вставку
    result = await collection.update_one(
        filter_condition,
        {"$set": grade_data_dict},
        upsert=True
    )
    return result
