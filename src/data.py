import json
from .habits import Habit
from .streaks import Streak
import datetime

# name of the file to save the data inside
DATA_FILE = "data.json"

def load_habits_from_dict(habits : dict):
    """
    loads all the habits from the json object (coverts dict objects to Habit options)

    Returns
    -------
    list[Habit]
    """
    items = habits.items()
    habits = []

    for habit_name, details in items:
        habits.append(load_habit_from_dict(habit_name, details))

    return habits

def load_habit_from_dict(habit_name : str, details : dict):
    """
    load a dict from a json object

    Parameters
    ----------
    habit_name : str,
        the name of the habit

    details : dict,
        the details of the affiliated habit

    Returns
    -------
    (Habit, list[Streak])
    """
    habit = Habit(habit_name, details["description"], details["periodicity"])
    streaks = load_streaks_from_list(habit, details["streaks"])
    return habit, streaks

def load_streaks_from_list(habit : Habit, streaks_dict: list[dict]) -> list[Streak]:
    """
    loads streaks from a list of dicts

    returns
    -------
    list[Streak]
    """
    streaks = []

    for streak in streaks_dict:
        streaks.append(
            Streak(
                habit, 
                datetime.date.fromisoformat(streak["start_date"]),
                datetime.date.fromisoformat(streak["end_date"])
            )
        )

    return streaks


def load_all_data():
    """
    Loads all the data present
    """
    with open(DATA_FILE) as f:
        data = json.load(f)

    habits = load_habits_from_dict(data['habits'])

    return habits

def habit_and_streaks_to_dict(habits_and_streaks : list[tuple[Habit, list[Streak]]]):
    """
    converts habits and streaks to a dictionary object

    Parameters
    ----------
    habits_and_streaks,
        a list of tuples of habits and streaks
    """
    info = {}

    for habit, streaks in habits_and_streaks:
        streaks_list = []

        for streak in streaks:
            streaks_list.append({
                "start_date" : streak.start_date.isoformat(),
                "end_date" : streak.end_date.isoformat()
            })

        info[habit.name] = {
            "description" : habit.description,
            "periodicity" : habit.periodicty,
            "streaks" : streaks_list
        }

    return info

def save_all_data(habits_and_streaks : list[tuple[Habit, list[Streak]]]):
    """
    saves all the data in the data.json file

    Parameters
    ----------
    habits_and_streaks,
        a list of tuples of habits and streaks
    """
    _dict = {
        "habits" : habit_and_streaks_to_dict(habits_and_streaks)
    }

    with open(DATA_FILE, "w") as f:
        json.dump(_dict, f, indent=2)

    return 