from typing import Union, List, Dict
from datetime import datetime
from pydantic import BaseModel, Field, field_validator

class GroupIDResponseSchema(BaseModel):
    message: str
    data: int


class LessonAddSchema(BaseModel):
    discipline: str
    auditorium: str
    date: str
    dayOfWeek: int
    beginLesson: str
    endLesson: str
    kindOfWork: str
    lecturer: str
    group_id: str


class LessonSchema(BaseModel):
    discipline: str
    auditorium: str
    date: str
    dayOfWeek: int
    beginLesson: str
    endLesson: str
    kindOfWork: str
    lecturer: str



class ScheduleResponseSchema(BaseModel):
    message: str
    data: Union[Dict[str, List[LessonSchema]],str]


class ScheduleRequestSchema(BaseModel):
    group_id: str
    date_start: datetime = Field(..., description="Дата начала в формате yyyy-mm-dd")
    date_end: datetime = Field(..., description="Дата окончания в формате yyyy-mm-dd")

    @field_validator('date_start', 'date_end')
    def validate_date_format(cls, value):
        # Преобразование в строку в формате 'yyyy-mm-dd'
        if isinstance(value, datetime):
            return value.date().strftime('%Y-%m-%d')
        return value

    class Config:
        # Задать формат даты для сериализации
        json_encoders = {
            datetime: lambda v: v.strftime('%Y-%m-%d')
        }

