from bs4 import BeautifulSoup
from ..utils.grades import get_student_info, get_subject_info
from ..schemas.user import LoginResponse

async def get_html(client, redirect_url):
    redirect_response = await client.get(redirect_url)
    redirect_response.raise_for_status()
    html_content = redirect_response.text
    return html_content

def get_bars_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    student_info = get_student_info(soup)
    subjects = get_subject_info(soup)

    # Create final response model
    result = LoginResponse(
        studentInfo=student_info,
        subjects=subjects
    )

    return result
