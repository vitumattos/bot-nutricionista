from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models.base_model import Base
from src.models.user import User
from src.models.diet_plan import DietPlan
from src.models.meal_entry import MealEntry
from src.models.report import Report
from src.models.weight_history import WeightHistory

from src.settings import DATABASE_URL


class Engine:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

