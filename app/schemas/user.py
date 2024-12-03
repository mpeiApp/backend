from pydantic import BaseModel, Field
from typing import List
from ..schemas.grades import Subject

class LoginModel(BaseModel):
    username: str
    password: str

class StudentInfo(BaseModel):
    login: str
    name: str
    surname: str
    groupNumber: str

class PersonGradesInfo(BaseModel):
    studentInfo: StudentInfo
    subjects: List[Subject] = Field(default_factory=list)
