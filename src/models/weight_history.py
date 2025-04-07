from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone
from src.models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class WeightHistorySchema(BaseModel):
    id: int
    telegram_id: int
    date: datetime = datetime.now(timezone.utc)
    weight_kg: Optional[int]
    extra_info: Optional[str]

    class Config:
        from_attributes = True


class WeightHistory(Base):
    __tablename__ = "weight_history"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    telegram_id = Column(Integer, ForeignKey('users.telegram_id'))
    date = Column(String, default=datetime.now(timezone.utc))
    weight_kg = Column(String)
    extra_info = Column(String, nullable=True)

    def to_pydantic(self):
        return WeightHistorySchema(**self.__dict__)
