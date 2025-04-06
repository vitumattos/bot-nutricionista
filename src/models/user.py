from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    id: int
    telegram_id: int
    name: str
    sex: str
    age: str
    height_cm: str
    weight_kg: str
    has_diabetes: str
    goal: str
    extra_info: Optional[str]
