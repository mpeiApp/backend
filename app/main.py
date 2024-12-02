from contextlib import asynccontextmanager

from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.api.endpoints.user import router as user_router
from app.api.endpoints.grades import router as grades_router
from app.db.database import init_db, client
from app.core.config import settings

from app.services.gradesScheduler import grades_job


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    scheduler = AsyncIOScheduler()
    await grades_job()
    scheduler.add_job(grades_job, 'interval', hours=int(settings.TIME_PARSE_GRADES), max_instances=24)
    scheduler.start()
    yield
    if client:
        await client.close()

app = FastAPI(lifespan=lifespan)

app.include_router(user_router, prefix="/user")
app.include_router(grades_router, prefix="/grades")
