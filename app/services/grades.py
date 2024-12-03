from bs4 import BeautifulSoup
from ..utils.grades import parse_student_info, parse_subject_info
from ..schemas.user import PersonGradesInfo

async def get_html(client, redirect_url):
    redirect_response = await client.get(redirect_url)
    redirect_response.raise_for_status()
    html_content = redirect_response.text
    return html_content

def get_bars_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    student_info = parse_student_info(soup)
    subjects = parse_subject_info(soup)

    # Create final response model
    result = PersonGradesInfo(
        studentInfo=student_info,
        subjects=subjects
    )

    return result

def get_student_info(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    student_info = parse_student_info(soup)
    return student_info