from pymongo.results import UpdateResult

from app.db.database import get_user_collection
from app.schemas.user import LoginModel


async def add_person(user_data: LoginModel) -> UpdateResult:
    collection = await get_user_collection()

    # Преобразуем объект в словарь
    user_data_dict = user_data.dict()

    # Условие фильтрации для обновления
    filter_condition = {
        "username": user_data.username,
    }

    # Выполняем обновление или вставку
    result = await collection.update_one(
        filter_condition,
        {"$set": user_data_dict},
        upsert=True
    )
    return result