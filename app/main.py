from fastapi import FastAPI
from app.api.endpoints.user import router as user_router
from app.api.endpoints.grades import router as grades_router

app = FastAPI()

app.include_router(user_router, prefix="/user")
app.include_router(grades_router, prefix="/grades")
