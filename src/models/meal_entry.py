from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone


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