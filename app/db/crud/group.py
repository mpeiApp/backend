from pymongo.results import UpdateResult

from app.db.database import get_group_collection
from app.schemas.group import GroupModel


async def add_group(group_data: GroupModel) -> UpdateResult:
    collection = await get_group_collection()

    # Преобразуем объект в словарь
    group_data_dict = group_data.dict()

    # Условие фильтрации для обновления
    filter_condition = {
        "groupNumber": group_data.groupNumber,
    }

    # Выполняем обновление или вставку
    result = await collection.update_one(
        filter_condition,
        {"$set": group_data_dict},
        upsert=True
    )
    return result