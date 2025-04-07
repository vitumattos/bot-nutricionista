from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone
from src.models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class ReportSchema(BaseModel):
    id: int
    telegram_id: int
    data: datetime = datetime.now(timezone.utc)
    report_details: str
    extra_info: Optional[str]

    class Config:
        from_attributes = True 

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    telegram_id = Column(Integer, ForeignKey('users.telegram_id'))
    data = Column(String, default=datetime.now(timezone.utc))
    report_details = Column(String)
    extra_info = Column(String, nullable=True)

    def to_pydantic(self):
        return ReportSchema(**self.__dict__)