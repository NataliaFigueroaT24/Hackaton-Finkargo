from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class SupportCaseBase(BaseModel):
    title: str
    description: str
    status: Optional[str] = "Open"

class SupportCaseCreate(SupportCaseBase):
    pass

class SupportCase(SupportCaseBase):
    case_id: int
    created_at: datetime
    updated_at: datetime
    user_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int
    created_at: datetime
    updated_at: datetime
    support_cases: List[SupportCase] = []

    class Config:
        orm_mode = True
