from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone

class DietPlanSchema(BaseModel):
    id: int
    telegram_id: int
    created_at: datetime = datetime.now(timezone.utc)
    plan_details: str
    extra_info: Optional[str]