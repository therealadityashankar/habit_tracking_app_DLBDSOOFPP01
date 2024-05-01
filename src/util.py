"""
utilities for easy coding of the rest of the files
"""

from .habits import Habit
from .streaks import Streak
from .analytics import HabitAnalytics
from . import prompts
import datetime

TEST_MODE : bool = False
TEST_CURRENT_DATE : datetime.date = None

def get_current_date():
    """
    This is a function to enable testing in the habit tracking app

    returns the current date in production mode
    otherwise, returns the asked for test date
    """
    if TEST_MODE:
        return TEST_CURRENT_DATE
    else:
        return datetime.date.today()
    
def get_yesterday_date():
    """
    This is a convinience function to get yesterday's date
    """
    return get_current_date() - datetime.timedelta(days=1)
    
def ask_current_date():
    """
    asks the current date, useful for testing
    """
    print("you're currently in test mode")
    print("-----------------------------")
    current_year  = int(input("Enter the current year : "))
    current_month = int(input("Enter the current month : "))
    current_day   = int(input("Enter the current day : "))
    date = datetime.date(year=current_year, month=current_month, day=current_day)
    print("-----------------------------")
    print(f"retrieved date is {date}")
    return date
    


def input_choice(choice_prompt : str):
    """
    adds a prompt, then asks the user for a choice to add, then returns it

    returns
    -------
    str
    """
    print(choice_prompt)
    return input("choice : ")

def pretty_print_habits_and_analytics(habits : list[tuple[Habit, list[Streak]]]):
    """
    prints the habits present in a very pretty manner

    Parameters
    ----------
    habits,
        a list of habits of the user
    """

    for habit, streaks in habits:
        analytics = get_habit_analytics(habit, streaks)

        print(habit.name)
        print(f"   {habit.description}")
        print(f"   periodicity : {habit.periodicty}")
       
        if len(streaks) > 0:

            print()
            print(f"   current streak : {streaks[-1].start_date} - {streaks[-1].end_date}")

            if habit.periodicty == "daily":
                num_days = streaks[-1].num_streak_days
                print(f"   days complete : {num_days} day{'s' if num_days > 1 else ''}")

                if streaks[-1].end_date == get_current_date():
                    print(f"   last marked today")
                    print()
                
                elif streaks[-1].end_date == get_yesterday_date():
                    print(f"   last marked yesterday")
                    print()

                else:
                    print(f"   last marked {streaks[-1].end_date}, streak broken!")
                    print()
            else:
                num_weeks = streaks[-1].num_streak_weeks
                print(f"   weeks complete : {num_weeks} week{'s' if num_weeks > 1 else ''}")

                # if the streak was last marked the last day
                # of last week, the streak goes on
                last_week_end = first_day_of_week(get_current_date()) - datetime.timedelta(days=1)
                this_week_end = last_week_end + datetime.timedelta(days=7)

                if streaks[-1].end_date == last_week_end:
                    print(f"   last marked last week")
                    print()
                
                elif streaks[-1].end_date == this_week_end:
                    print(f"   last marked this week")
                    print()

                else:
                    print(f"   last marked {streaks[-1].end_date}, streak broken!")
                    print()

            print(f"   longest streak : {analytics.longest_streak_start} - {analytics.longest_streak_end}")
            
            if habit.periodicty == 'daily':
                print(f"   longest streak days complete : {analytics.longest_streak_days} day{'s' if analytics.longest_streak_days > 1 else ''}")
                print()
            else:
                print(f"   longest streak weeks complete : {analytics.longest_streak_weeks} week{'s' if analytics.longest_streak_weeks > 1 else ''}")
                print()
        else:
            print(f"   *no streak yet!")
        print()

    return

def create_new_habit(habits_and_streaks : list[tuple[Habit, list[Streak]]]):
    """
    gives an input to creating a new habit

    Parameters
    ----------
    habits_and_streaks : list,
        the list of all habits

    """
    habit = input("Enter habit name: ")
    description = input("Enter a description for the habit: ")
    periodicity_option = input_choice(prompts.CHOICE_DAILY_OR_WEEKLY_TASK)

    if periodicity_option == 'a':
        periodicity = 'daily'
    else:
        periodicity = 'weekly'

    habits_and_streaks.append((Habit(habit, description, periodicity), []))

def update_habit(habits_and_streaks : list[tuple[Habit, list[Streak]]]):
    """
    gives the user the choice to rename a habit

    Parameters
    ----------
    habits_and_streaks : list,
        the list of all habits
    """
    print("Choose a habit to modify:")
    
    for i, (habit, _) in enumerate(habits_and_streaks):
        print(f"{i + 1}: {habit.name} - {habit.description}")

    print()
    habit_num = input("Enter a number corresponding to the habit to modify: ")
    habit_num = int(habit_num) - 1

    habit, _ = habits_and_streaks[habit_num]

    print("----------------")
    print("Enter new habit name:")
    new_name = input("name : ")

    print("Enter new habit description:")
    new_desc = input("description : ")

    habit.name = new_name
    habit.description = new_desc

    print()
    print("successfully modified!")
    print("----------------------")
    print()

def delete_habit(habits_and_streaks : list[tuple[Habit, list[Streak]]]):
    """
    delete a specified habit by the user

    Parameters
    ----------
    habits_and_streaks : list,
        the list of all habits
    """
    print("choose a habit to delete")
    for i, (habit, _) in enumerate(habits_and_streaks):
        print(f"{i + 1}: {habit.name} - {habit.description}")

    print()
    habit_num = input("Enter a number corresponding to the habit to delete: ")
    habit_num = int(habit_num) - 1

    del habits_and_streaks[habit_num]

    print()
    print("successfully deleted!")
    print("----------------------")
    print()

def first_day_of_week(date : datetime.date):
    """
    gets the first day of the corresponding week, for a particular day
    """
    # Get the weekday (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    weekday = date.weekday()
    # Calculate the difference from the current day to Monday
    days_to_monday = weekday
    # Get the date for Monday of the current week
    first_day = date - datetime.timedelta(days=days_to_monday)
    return first_day

def mark_habit_as_complete(habits_and_streaks : list[tuple[Habit, list[Streak]]]):
    """
    mark a specified habit as complete

    Parameters
    ----------
    habits_and_streaks : list,
        the list of all habits
    """
    print("Choose a habit to mark as complete:")
    
    for i, (habit, streaks) in enumerate(habits_and_streaks):
        suffix_text = ""

        if len(streaks) > 0:
            if habit.periodicty == "daily":
                if streaks[-1].end_date == get_current_date():
                    suffix_text = "(last marked today)"
                
                elif streaks[-1].end_date == get_yesterday_date():
                    suffix_text = "(last marked yesterday)"

                else:
                    suffix_text = f"(last marked {streaks[-1].end_date}, streak broken!)"
            else:
                # if the streak was last marked the last day
                # of last week, the streak goes on
                last_week_end = first_day_of_week(get_current_date()) - datetime.timedelta(days=1)
                this_week_end = last_week_end + datetime.timedelta(days=7)

                if streaks[-1].end_date == last_week_end:
                    suffix_text = "(last marked last week)"
                
                elif streaks[-1].end_date == this_week_end:
                    suffix_text = "(last marked this week)"

                else:
                    suffix_text = f"(last marked {streaks[-1].end_date}, streak broken!)"

        print(f"{i + 1}: ({habit.periodicty}) {habit.name} - {habit.description} {suffix_text}")

    print()
    habit_num = input("Enter a number corresponding to the habit to mark as complete for today: ")
    habit_num = int(habit_num) - 1

    habit, streaks = habits_and_streaks[habit_num]

    # if streaks is empty,
    # or if the last streak day is a day before yesterday
    # create a new streak round
    if len(streaks) == 0:
        if habit.periodicty == "daily":
            streaks.append(Streak(habit, get_current_date(), get_current_date()))
        else:
            this_week_start = first_day_of_week(get_current_date())
            this_week_end = last_week_end + datetime.timedelta(days=7)
            streaks.append(Streak(habit, this_week_start, this_week_end))
    else:

        if habit.periodicty == "daily":
            # check if the last streak is one day old
            if (get_current_date() - streaks[-1].end_date).days == 1:
                # set it as today's date
                streaks[-1].end_date = get_current_date()
                print(f"amazing, you've completed the streak for {streaks[-1].num_streak_days} day{'s' if streaks[-1].num_streak_days > 1 else ''} now!")

            elif get_current_date() == streaks[-1].end_date:
                print("you've already marked this streak as complete for today!")
                print(f"you've completed the streak for {streaks[-1].num_streak_days} day{'s' if streaks[-1].num_streak_days > 1 else ''} now!")

            else:
                print("you're starting a new streak, you got this!")
                streaks.append(Streak(habit, get_current_date(), get_current_date()))
        else:
            # if the streak was last marked the last day
            # of last week, the streak goes on
            this_week_start = first_day_of_week(get_current_date())
            last_week_end = this_week_start - datetime.timedelta(days=1)
            this_week_end = last_week_end + datetime.timedelta(days=7)

            if streaks[-1].end_date == last_week_end:
                # set it as complete for this week
                streaks[-1].end_date = this_week_end
                print(f"amazing, you've completed the streak for {streaks[-1].num_streak_weeks} week{'s' if streaks[-1].num_streak_weeks > 1 else ''} now!")
            
            elif streaks[-1].end_date == this_week_end:
                print("you've already marked this streak as complete for this week!")
                print(f"you've completed the streak for {streaks[-1].num_streak_weeks} week{'s' if streaks[-1].num_streak_weeks > 1 else ''} now!")

            else:
                print("you're starting a new streak, you got this!")
                streaks.append(Streak(habit, this_week_start, this_week_end))

    print()
    if habit.periodicty == "daily":
        print("successfully marked habit as complete for today!")
    else:
        print("successfully marked habit as complete for this week!")
    print("----------------------")
    print()


def get_habit_analytics(habit : Habit, streaks : list[Streak]) -> HabitAnalytics:
    """
    return a habit analytics object having analytics with regard to the current habits

    Parameters
    ----------
    habit : Habit,
        the current habit to get analytics on

    streaks : list[Streak],
        all the streaks related to the habit
    """
    longest_streak = None
    longest_streak_days = 0

    if len(streaks) > 0:
        current_streak = streaks[-1]

        for streak in streaks:
            if streak.num_streak_days >= longest_streak_days:
                longest_streak = streak
                longest_streak_days = streak.num_streak_days
    else:
        current_streak = None
    
    if len(streaks) > 0:
        return HabitAnalytics(current_streak, longest_streak.start_date, longest_streak.end_date)
    else:
        return HabitAnalytics(None, None, None)