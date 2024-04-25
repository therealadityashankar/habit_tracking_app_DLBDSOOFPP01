from dataclasses import dataclass
from .habits import Habit
import datetime
import math

@dataclass
class Streak:
    """
    Represents streaks a user may have for tracking habits.

    Parameters
    ----------
    habit (Habit): An instance of the habit class
    start_date (datetime.date): The start date of the streak.
    end_date (datetime.date): The current streak of the habit.
    """
    habit: Habit
    start_date: datetime.date
    end_date: datetime.date

    @property
    def num_streak_days(self):
        return (self.end_date - self.start_date).days + 1
    
    @property
    def num_streak_weeks(self):
        return math.ceil(self.num_streak_days/7)