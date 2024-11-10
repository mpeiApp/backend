from pydantic import BaseModel, Field
from typing import List
from ..schemas.grades import Subject

class UserModel(BaseModel):
    username: str
    password: str


class StudentInfo(BaseModel):
    name: str
    surname: str
    groupNumber: str

class LoginResponse(BaseModel):
    studentInfo: StudentInfo
    subjects: List[Subject] = Field(default_factory=list)
