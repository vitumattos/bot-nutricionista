from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone
from src.models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class MealEntrySchema(BaseModel):
    id: int
    telegram_id: int
    timestamp: datetime = datetime.now(timezone.utc)
    meal_description: str
    image_path: Optional[str]
    calories: Optional[int]
    carbs: Optional[int]
    proteins: Optional[int]
    fats: Optional[int]
    extra_info: Optional[str]

    class Config:
        from_attributes = True


class MealEntry(Base):
    __tablename__ = "meal_entries"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    telegram_id = Column(Integer, ForeignKey('users.telegram_id'))
    timestamp = Column(String, default=datetime.now(timezone.utc))
    meal_description = Column(String)
    image_path = Column(String, nullable=True)
    calories = Column(String, nullable=True)
    carbs = Column(String, nullable=True)
    proteins = Column(Integer, nullable=True)
    fats = Column(String, nullable=True)
    extra_info = Column(String, nullable=True)

    def to_pydantic(self):
        return MealEntrySchema(**self.__dict__)
