from fastapi import FastAPI
from app.api.endpoints.schedule import router as schedule_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url="/docs", redoc_url="/redoc")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(schedule_router, prefix="/schedule")
