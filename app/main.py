from fastapi import FastAPI
from app.api.endpoints.schedule import router as schedule_router
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.db.database import init_db, client
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import timedelta
# from app.services.scheduleScheduler import schedule_job
import os
from app.core.config import settings

from app.services.scheduleScheduler import schedule_job


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(settings.DATABASE_URL, settings.DATABASE_NAME)
    await init_db()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(schedule_job, 'interval', seconds=int(settings.TIME_PARSE_SCHEDULE), max_instances=10)
    scheduler.start()
    yield
    if client:
        await client.close()

app = FastAPI(lifespan=lifespan)

app.include_router(schedule_router, prefix="/schedule")





