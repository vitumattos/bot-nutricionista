from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone

class ReportSchema(BaseModel):
    id: int
    telegram_id: int
    data: datetime = datetime.now(timezone.utc)
    report_details: str
    extra_info: Optional[str]