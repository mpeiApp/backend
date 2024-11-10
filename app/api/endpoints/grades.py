from fastapi import APIRouter

from app.services.grades import get_bars_data
from app.services.login import login_to_bars
from app.schemas.user import UserModel

router = APIRouter()

@router.post("/grades")
async def root(model: UserModel):
    result = await login_to_bars(model.username, model.password)
    if result['message'] == 'OK':
        html_content = result['html_content']
        return get_bars_data(html_content)
