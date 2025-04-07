from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, ForeignKey
from src.models.base_model import Base

class DietPlanSchema(BaseModel):
    id: int
    telegram_id: int
    created_at: datetime = datetime.now(timezone.utc)
    plan_details: str
    extra_info: Optional[str]

    class Config:
        from_attributes = True

class DietPlan(Base):
    __tablename__ = "diet_plans"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    telegram_id = Column(Integer, ForeignKey('users.telegram_id'))
    created_at = Column(String, default=datetime.now(timezone.utc))
    plan_details = Column(String)
    extra_info = Column(String, nullable=True)

    def to_pydantic(self):
        return DietPlanSchema(**self.__dict__)