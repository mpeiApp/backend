from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
from pymongo.errors import ConnectionFailure

client: AsyncIOMotorClient = None
database = None

async def init_db():
    global client, database
    try:
        client = AsyncIOMotorClient(settings.DATABASE_URL)
        database = client.get_database(settings.DATABASE_NAME)
        print('[INFO] Connection established')
    except ConnectionFailure:
        print("[ERROR] Failed to connect to MongoDB")


def get_collection(collection_name: str):
    if database is None:
        raise Exception("Database is not initialized")
    return database[collection_name]


async def get_user_collection():
    return get_collection("users")


async def get_schedule_collection():
    return get_collection("schedule")
