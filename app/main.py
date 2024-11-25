from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.api.endpoints.user import router as user_router
from app.api.endpoints.grades import router as grades_router
from app.db.database import init_db, client


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    if client:
        await client.close()

app = FastAPI(lifespan=lifespan)

app.include_router(user_router, prefix="/user")
app.include_router(grades_router, prefix="/grades")
