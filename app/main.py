from fastapi import FastAPI
from app.api.endpoints.schedule import router as schedule_router

app = FastAPI()

app.include_router(schedule_router, prefix="/schedule")
