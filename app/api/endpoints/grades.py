from fastapi import APIRouter

from app.db.crud.grades import add_person_grades
from app.services.grades import get_bars_data
from app.services.login import login_to_bars
from app.schemas.user import UserModel

router = APIRouter()

@router.post("/grades")
async def root(model: UserModel):
    result = await login_to_bars(model.username, model.password)
    if result['message'] == 'OK':
        html_content = result['html_content']
        return {"message": "OK",
                "data": get_bars_data(html_content)}
    return {"message": "NOT OK",
            "data": None}

@router.post("/add_grades")
async def root(model: UserModel):
    result = await login_to_bars(model.username, model.password)
    if result['message'] == 'OK':
        html_content = result['html_content']
        person_grades_info = get_bars_data(html_content)

        response = await add_person_grades(person_grades_info)

        return {"message": "OK",
                "data": None,
                "isUpdated": response.raw_result.get("updatedExisting", False)}
    return {"message": "NOT OK",
            "data": None,
            "isUpdated": None}
