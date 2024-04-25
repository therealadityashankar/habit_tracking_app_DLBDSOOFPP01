from .streaks import Streak
from dataclasses import dataclass
import datetime
import math

@dataclass
class HabitAnalytics:
    """
    analytics with regard to the habit present

    Properties
    ----------
    current_streak (Streak) : the current streak
    longest_streak_start : the start date for the longest streak
    longest_streak_end : the end date for the longest streak    
    """
    current_streak : Streak
    longest_streak_start : datetime.date
    longest_streak_end : datetime.date

    @property
    def longest_streak_days(self):
        return (self.longest_streak_end - self.longest_streak_start).days + 1
    
    @property
    def longest_streak_weeks(self):
        return math.ceil(self.longest_streak_days/7)
    
    @property
    def current_streak_days(self):
        return self.current_streak.num_streak_days
    
    @property
    def current_streak_weeks(self):
        return self.current_streak_weeks