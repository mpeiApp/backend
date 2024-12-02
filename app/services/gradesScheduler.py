import asyncio
import os
from datetime import datetime

from app.db.crud.grades import add_person_grades
from app.db.database import database, get_grades_collection
from app.services.grades import get_bars_data
from app.services.login import login_to_bars

username = "gusakAN"
password = "gab621z"

async def grades_job():
    result = await login_to_bars(username, password)
    if result['message'] == 'OK':
        html_content = result['html_content']
        person_grades_info = get_bars_data(html_content)

        response = await add_person_grades(person_grades_info)