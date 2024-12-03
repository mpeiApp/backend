from fastapi import APIRouter

from app.db.crud.group import add_group
from app.db.crud.user import add_person
from app.schemas.group import GroupModel
from app.services.grades import get_student_info
from app.services.login import login_to_bars
from app.schemas.user import LoginModel
from app.services.schedule import get_group_id

router = APIRouter()

@router.post("/login")
async def login(model: LoginModel):
    try:
        result = await login_to_bars(model.username, model.password)
        if result['message'] == 'OK':
            html_content = result['html_content']
            student_info = get_student_info(html_content)

            response = await get_group_id(student_info.groupNumber)

            if response['message'] == 'ok':
                group_internal_id = response['data']

                response = await add_person(model)

                group_model = GroupModel(groupNumber=student_info.groupNumber,
                                         group_internal_id=group_internal_id)
                response = await add_group(group_model)

                return {
                    "message": "OK",
                    "data": group_internal_id,

                }
            else:
                return {
                    "message": "NOT OK",
                    "data": None,
                    "error": response
                }
        else:
            return {
                "message": "NOT OK",
                "data": None
            }
    except Exception as e:
        # return {"error": str(e)}
        return {
            "message": f"NOT OK",
            "data": str(e)
        }

@router.post("/login/htmlcontent")
async def login_to_bars_and_get_htmlcontent(model: LoginModel):
    try:
        result = await login_to_bars(model.username, model.password)
        # return result
        return {
            "message": "OK",
            "data": result
        }
    except Exception as e:
        # return {"error": str(e)}
        return {
            "message": f"NOT OK",
            "data": str(e)
        }

@router.get("/get_student_info")
async def get_student_info_from_bars(username, password):
    result = await login_to_bars(username, password)
    if result['message'] == 'OK':
        html_content = result['html_content']
        return {"message": "OK",
                "data": get_student_info(html_content)}
    return {"message": "NOT OK",
            "data": None}

@router.post("/add_user")
async def add_user(model: LoginModel):
    try:
        response = await add_person(model)
        return {"message": "OK",
                "data": None,
                "isUpdated": response.raw_result.get("updatedExisting", False)}
    except Exception as e:
        return {"message": f"NOT OK",
                'exception': str(e)}