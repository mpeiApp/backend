from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.api.endpoints.schedule import router as schedule_router
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.db.database import init_db, client

from app.api.endpoints.user import router as user_router
from app.api.endpoints.grades import router as grades_router
from app.api.endpoints.group import router as group_router

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import timedelta
# from app.services.scheduleScheduler import schedule_job
import os
from app.core.config import settings

from app.services.gradesScheduler import grades_job

from app.services.scheduleScheduler import schedule_job


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(settings.DATABASE_URL, settings.DATABASE_NAME)
    await init_db()
    await grades_job()
    await schedule_job()

    scheduler = AsyncIOScheduler()
    scheduler.add_job(grades_job, 'interval', hours=int(settings.TIME_PARSE_GRADES), max_instances=24)
    scheduler.add_job(schedule_job, 'interval', hours=int(settings.TIME_PARSE_SCHEDULE), max_instances=10)
    scheduler.start()
    yield
    if client:
        await client.close()

app = FastAPI(lifespan=lifespan)

app.include_router(schedule_router, prefix="/schedule")

app.include_router(user_router, prefix="/user")
app.include_router(grades_router, prefix="/grades")
app.include_router(group_router, prefix="/group")
