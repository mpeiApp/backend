from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date


class Grade(BaseModel):
    name: str
    weight: int
    weekNumber: int
    dateStart: Optional[date]
    dateEnd: date
    mark: Optional[int]
    markDate: Optional[date]


class Subject(BaseModel):
    name: str
    teacher: str
    averageGrade: float
    examinationType: str
    gradeList: List[Grade] = Field(default_factory=list)

