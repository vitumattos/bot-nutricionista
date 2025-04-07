from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String
from src.models.base_model import Base


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

    class Config:
        from_attributes = True


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    telegram_id = Column(Integer)
    name = Column(String)
    sex = Column(String)
    age = Column(String)
    height_cm = Column(String)
    weight_kg = Column(String)
    has_diabetes = Column(String)
    goal = Column(String)
    extra_observations = Column(String, nullable=True)

    def to_pydantic(self):
        return UserSchema(**self.__dict__)
