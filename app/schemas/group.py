from pydantic import BaseModel


class GroupModel(BaseModel):
    group_internal_id: int
    groupNumber: str