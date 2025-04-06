from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone

class WeightHistorySchema(BaseModel):
    id: int
    telegram_id: int
    date: datetime = datetime.now(timezone.utc)
    weight_kg: Optional[int]
    extra_info: Optional[str]