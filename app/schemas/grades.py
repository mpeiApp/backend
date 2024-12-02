from pydantic import BaseModel, Field
from typing import List, Optional


class Grade(BaseModel):
    name: str
    weight: int
    weekNumber: int
    dateStart: Optional[str]
    dateEnd: str
    mark: Optional[int]
    markDate: Optional[str]


class Subject(BaseModel):
    name: str
    teacher: str
    averageGrade: float
    examinationType: str
    gradeList: List[Grade] = Field(default_factory=list)

