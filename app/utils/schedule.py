import httpx


class Lesson:
    def __init__(self, discipline, auditorium, date, dayOfWeek, time_begin, time_end, kindOfWork, lecturer):
        self.discipline = discipline
        self.auditorium = auditorium
        self.date = date
        self.dayOfWeek = dayOfWeek
        self.time_begin = time_begin
        self.time_end = time_end
        self.kindOfWork = kindOfWork
        self.lecturer = lecturer

    def __str__(self):
        return f"{self.time_begin} - {self.time_end}\n" \
               f"{self.discipline} - {self.kindOfWork}\n" \
               f"{self.auditorium}\n" \
               f"Преподаватель - {self.lecturer}"

    def to_dict(self):
        return {
            "discipline": self.discipline,
            "auditorium": self.auditorium,
            "date": self.date,
            "dayOfWeek": self.dayOfWeek,
            "time_begin": self.time_begin,
            "time_end": self.time_end,
            "kindOfWork": self.kindOfWork,
            "lecturer": self.lecturer
        }

async def get_schedule(group_id, date_start, date_end):
    URL = f'http://ts.mpei.ru/api/schedule/group/{group_id}?start={date_start}&finish={date_end}&lng=1'
    async with httpx.AsyncClient() as client:
        response = await client.get(URL)
        if response.status_code == 200:
            responseData = response.json()
            if len(responseData) != 0 and 'error' not in responseData:
                return {
                    'message': "ok",
                    'data': responseData
                }
            else:
                if 'error' in responseData:
                    return {
                        'message': "not ok",
                        'data': responseData['error']
                    }
                return {
                    'message': "not ok",
                    'data': "empty schedule",
                }
        return {
            'message': "not ok",
            'data': response.status_code
        }


async def form_schedule(data):
    weekSchedule = {}

    lessons_class = []
    for lesson in data:
        current_lesson = Lesson(
            lesson['discipline'],
            lesson['auditorium'],
            lesson['date'],
            lesson['dayOfWeek'],
            lesson['beginLesson'],
            lesson['endLesson'],
            lesson['kindOfWork'],
            lesson['lecturer'],
        )

        if lesson['date'] not in weekSchedule:
            weekSchedule[lesson['date']] = [current_lesson.to_dict()]
        else:
            weekSchedule[lesson['date']].append(current_lesson.to_dict())

        lessons_class.append(current_lesson.to_dict())
    return weekSchedule
