from ..schemas.grades import Subject, Grade
from ..schemas.user import StudentInfo
from datetime import datetime

# Parse student info
def get_student_info(soup):
    student_info_text = soup.find('span', class_='fw-bold').text.strip()
    surname, name, middle_name, *_, group_number = student_info_text.split(' ')
    student_info = StudentInfo(
        name=name,
        surname=surname,
        groupNumber=group_number
    )
    return student_info


# Parse subjects
def get_subject_info(soup):
    subjects = []
    subject_elements = soup.find_all('div', {'data-bs-toggle': 'collapse'})
    for subject_html in subject_elements:
        subject_info = subject_html.get_text(strip=True, separator=' ')
        if subject_info != "(критерии)":
            subject_name, teacher, exam_type, *_ = subject_info.split(", ")
            subjects.append(Subject(name=subject_name,
                                    teacher=teacher,
                                    examinationType=exam_type,
                                    averageGrade=0.0,
                                    gradeList=[]))

    # Parse grades
    tables_marks = soup.find_all(class_='collapse')
    i = 0
    for table_marks in tables_marks:
        table_html = table_marks.find('table')
        if table_html:
            for row in table_html.find_all('tr'):
                cols = row.find_all('td')
                if len(cols) == 2 and cols[0].get_text(strip=True) == "Балл текущего контроля:":
                    subjects[i].averageGrade = float(cols[1].get_text(strip=True).replace(",", "."))
                if len(cols) < 4:
                    continue

                grade = get_grade_info(cols)
                subjects[i].gradeList.append(grade)
            i += 1

    return subjects


# Parse grade
def get_grade_info(cols):
    name = cols[0].get_text(strip=True).split("(критерии)")[0]
    weight = cols[1].get_text(strip=True)
    date_conduct = cols[2].get_text(strip=True)
    week_number, date_range = date_conduct.split(" ")
    if len(date_range[1:-1].split("-")) == 2:
        date_start, date_end = date_range[1:-1].split("-")
        date_start = datetime.strptime(date_start, "%d.%m.%y").date()
        date_end = datetime.strptime(date_end, "%d.%m.%y").date()
    else:
        date_end = date_range[1:-1]
        date_end = datetime.strptime(date_end, "%d.%m.%y").date()
        date_start = None
    grade_date = cols[3].get_text(strip=True)
    mark = None
    mark_date = None
    if grade_date:
        mark = grade_date.split(" ")[0]
        mark_date = grade_date.split(" ")[-1][1:-1]
        mark_date = datetime.strptime(mark_date, "%d.%m.%y").date()

    grade = Grade(
        name=name,
        weight=weight,
        weekNumber=int(week_number),
        dateStart=date_start,
        dateEnd=date_end,
        mark=mark,
        markDate=mark_date
    )

    return grade