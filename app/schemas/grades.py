from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class Grade(BaseModel):
    name: str
    weight: int
    weekNumber: int
    dateStart: Optional[datetime]
    dateEnd: datetime
    mark: Optional[int]
    markDate: Optional[datetime]


class Subject(BaseModel):
    name: str
    teacher: str
    averageGrade: float
    examinationType: str
    gradeList: List[Grade] = Field(default_factory=list)

