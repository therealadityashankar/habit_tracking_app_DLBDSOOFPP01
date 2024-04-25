from dataclasses import dataclass

@dataclass
class Habit:
    """
    Represents a habit that a person wants to track and manage.

    Attributes:
        name (str): The name of the habit.
        description (str): A brief description of the habit.
        periodicty (str) : is this a 'weekly' or a 'daily' habit?
    """
    name: str
    description: str
    periodicty : str