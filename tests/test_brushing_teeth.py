"""
The files to test all the code in the code base

the 'mock_input' function overrides the input function in the code, 
to be able to thoroughly test the codebase

Tests to check if the "brushing teeth" habit
1. Can be added
2. Can have the name and description changed
3. Can be marked as completed for the today, next day, and the day after
4. Can be not marked for 1 day, and thus cause a loss of a streak
5. Can have a successful 4 week streak
6. Can be removed
"""

import datetime
import textwrap
import unittest
from unittest.mock import patch
import io
import sys
import main
import json
import os

# Add the parent directory to sys.path
current_directory = os.path.abspath(os.path.dirname(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory) 

with open(os.path.join(parent_directory, "data.json")) as f:
    habits = json.load(f)["habits"]


# complete test CLI operations
complete_test_cli_operations = [
    # 1. Creating a new habit
    "2024", "04", "25", # the mock date setup
    "b", "b", "a", # selecting creating a new habit
    "test-brushing-teeth", # the name of the habit
    "testing brushing teeth in the morning", # the description of the habit
    "a", # selecting a daily habit

    # Checking if the habit is correctly set in analytics
    "2024", "04", "25", # the mock date setup
    "a", # selecting analytics

    # 2. Renaming a habit
    "2024", "04", "25", # the mock date setup
    "b", "b", "b", # selecting creating a new habit
    str(len(habits) + 1), # selecting the newest habit,
    "test-brushing-teeth-renamed",
    "testing brushing teeth in the morning", # the description of the habit,

    # Checking if the habit is correctly renamed in analytics
    "2024", "04", "25", # the mock date setup
    "a" # selecting analytics
]

# 3. adding a week of marking to the above list, to ensure that the habit
# can be correctly marked continuously for 3 days
for i in range(3):
    complete_test_cli_operations.extend([
        # marking the task
        "2024", "04", str(25 + i), # select the date, i.e. today, tomorrow or the day after
        "b", "a", # selecting marking a task
        str(len(habits) + 1), # selecting the task to mark
        "b", # just marking one task for now!

        # analysing if the task is correctly marked
        "2024", "04", str(25 + i), # the mock date setup
        "a", # selecting analytics
    ])

# 4. Can be not marked for 1 day, and thus cause a loss of a streak
complete_test_cli_operations.extend([
        # marking the task one day later
        "2024", "04", "29", # select the date, i.e. 29th (skipping the 28th)
        "b", "a", # selecting marking a task
        str(len(habits) + 1), # selecting the task to mark
        "b", # just marking one task for now!

        # analysing if the task is correctly marked
        # and the streak has been broken
        "2024", "04", str(29), # the mock date setup
        "a", # selecting analytics
])

# 5. Can have a successful 4 week streak
# adding a week of marking to the above list, to ensure that the habit
# can be correctly marked continuously for a 4 weeks
# first day was already marked in the previous step
for i in range(1, 28):
    date = datetime.date(2024, 4, 29) + datetime.timedelta(days=i)

    complete_test_cli_operations.extend([
        # marking the task
        str(date.year), str(date.month), str(date.day), # select the date, i.e. today, tomorrow or the day after
        "b", "a", # selecting marking a task
        str(len(habits) + 1), # selecting the task to mark
        "b", # just marking one task for now!
    ])

# check it
complete_test_cli_operations.extend([        
        # analysing if the task is correctly marked,
        # and a 4 week streak exists
        str(date.year), str(date.month), str(date.day), # the mock date setup
        "a", # selecting analytics
])

# 6. Remove the item
complete_test_cli_operations.extend([
    # marking the task
    str(date.year), str(date.month), str(date.day), # select the date, i.e. today, tomorrow or the day after
    "b", "b", "c", # delete the task
    str(len(habits) + 1) # selecting the task to delete
])

# check it
complete_test_cli_operations.extend([        
        # analysing if the task is correctly marked,
        # and a 4 week streak exists
        str(date.year), str(date.month), str(date.day), # the mock date setup
        "a" # selecting analytics
])

def mock_input(all_test_values : list[str]):
    """
    creates a mock input that gives the specified input values in the list back

    Parameters
    ----------
    all_test_values,
        a list of all test inputs
    """
    occurance_num = 0
    def real_mock_input(prompt):
        nonlocal occurance_num
        test_value = all_test_values[occurance_num]
        occurance_num += 1

        # Open the file in append mode. If the file doesn't exist, it will be created.
        with open("xyz.txt", "a") as file:
            # Write a new line containing 'abc' to the file.
            file.write("\n" + test_value)

        return test_value
    
    return real_mock_input

# Test case with custom side effect
class TestBrushingTeeth(unittest.TestCase):
    """

    in addition, analytics in each step above will be checked to
    ensure that each step is functioning properly
    """
    @classmethod
    def tearDownClass(cls) -> None:
        with open(os.path.join(parent_directory, "data.json"), "w") as f:
            json.dump({"habits":habits}, f)

    def step1_habit_creation_daily_test(self):
        """
        checks if daily habits can be successfully added or not
        """
        # prevents messy output leaking
        # creates a habit
        captured_output = io.StringIO()
        to_put_back = sys.stdout
        sys.stdout = captured_output
        main.main()
        sys.stdout = to_put_back

        # check if it has been added in analytics
        captured_output = io.StringIO()
        to_put_back = sys.stdout
        sys.stdout = captured_output
        main.main()
        output = captured_output.getvalue().strip() 
        sys.stdout = to_put_back

        output_should_contain = textwrap.dedent("""\
        test-brushing-teeth
           testing brushing teeth in the morning
           periodicity : daily
           *no streak yet!""")

        self.assertIn(output_should_contain, output)
    
    def step2_habit_renaming_test(self):
        """
        checks if habit has been successfully renamed or not
        """
        # prevents messy output leaking
        # renames a habit
        captured_output = io.StringIO()
        to_put_back = sys.stdout
        sys.stdout = captured_output
        main.main()
        sys.stdout = to_put_back

        # check if it has been added in analytics
        captured_output = io.StringIO()
        to_put_back = sys.stdout
        sys.stdout = captured_output
        main.main()
        output = captured_output.getvalue().strip() 
        sys.stdout = to_put_back

        output_should_contain = textwrap.dedent("""\
        test-brushing-teeth-renamed
           testing brushing teeth in the morning
           periodicity : daily
           *no streak yet!""")

        self.assertIn(output_should_contain, output)

    def step3_habit_marking_test(self):
        """
        checks if habit has been successfully marked or not
        """
        for i in range(3):
            # prevents messy output leaking
            # marks a habit as complete for the day
            captured_output = io.StringIO()
            to_put_back = sys.stdout
            sys.stdout = captured_output
            main.main()
            sys.stdout = to_put_back

            # check if it has been added in analytics
            captured_output = io.StringIO()
            to_put_back = sys.stdout
            sys.stdout = captured_output
            main.main()
            output = captured_output.getvalue().strip() 
            sys.stdout = to_put_back

            output_should_contain = textwrap.dedent(f"""\
            test-brushing-teeth-renamed
               testing brushing teeth in the morning
               periodicity : daily

               current streak : 2024-04-25 - 2024-04-{25 + i}
               days complete : {i + 1} day{"s" if i > 0 else ""}
               last marked today

               longest streak : 2024-04-25 - 2024-04-{25 + i}
               longest streak days complete : {i + 1} day{"s" if i > 0 else ""}""")

            self.assertIn(output_should_contain, output)
    
    def step4_habit_not_marking_test(self):
        """
        check if a habit is not marked successfully
        """
        # prevents messy output leaking
        # marks a habit as complete for the day
        captured_output = io.StringIO()
        to_put_back = sys.stdout
        sys.stdout = captured_output
        main.main()
        sys.stdout = to_put_back
        
        # check if it has been marked in analytics as
        # having a streak of only one day
        captured_output = io.StringIO()
        to_put_back = sys.stdout
        sys.stdout = captured_output
        main.main()
        output = captured_output.getvalue().strip() 
        sys.stdout = to_put_back

        output_should_contain = textwrap.dedent(f"""\
        test-brushing-teeth-renamed
           testing brushing teeth in the morning
           periodicity : daily

           current streak : 2024-04-29 - 2024-04-29
           days complete : 1 day
           last marked today

           longest streak : 2024-04-25 - 2024-04-27
           longest streak days complete : 3 days""")

        self.assertIn(output_should_contain, output)
    
    def step5_4_week_streak_test(self):
        """
        check if a 4 week streak can be added successfully
        """
        for i in range(27):
            # prevents messy output leaking
            # marks a habit as complete for the day
            captured_output = io.StringIO()
            to_put_back = sys.stdout
            sys.stdout = captured_output
            main.main()
            sys.stdout = to_put_back

        # check if it has been added in analytics
        captured_output = io.StringIO()
        to_put_back = sys.stdout
        sys.stdout = captured_output
        main.main()
        output = captured_output.getvalue().strip() 
        sys.stdout = to_put_back

        output_should_contain = textwrap.dedent(f"""\
        test-brushing-teeth-renamed
           testing brushing teeth in the morning
           periodicity : daily

           current streak : 2024-04-29 - 2024-05-26
           days complete : 28 days
           last marked today

           longest streak : 2024-04-29 - 2024-05-26
           longest streak days complete : 28 days""")
        
        self.assertIn(output_should_contain, output)
    
    def step6_habit_deletion_test(self):
        """
        test that the habit gets successfully deleted
        """
        # prevents messy output leaking
        # deletes the habit
        captured_output = io.StringIO()
        to_put_back = sys.stdout
        sys.stdout = captured_output
        main.main()
        sys.stdout = to_put_back

        # check if it has been added in analytics
        captured_output = io.StringIO()
        to_put_back = sys.stdout
        sys.stdout = captured_output
        main.main()
        output = captured_output.getvalue().strip() 
        sys.stdout = to_put_back

        output_should_not_contain = textwrap.dedent(f"test-brushing-teeth-renameds")
        self.assertNotIn(output_should_not_contain, output)
    
    @patch('builtins.input', side_effect=mock_input(complete_test_cli_operations))
    def test_brushing_teeth_habit(self, mock_input):
        self.step1_habit_creation_daily_test()
        self.step2_habit_renaming_test()
        self.step3_habit_marking_test()
        self.step4_habit_not_marking_test()
        self.step5_4_week_streak_test()
        self.step6_habit_deletion_test()
    

if __name__ == '__main__':
    unittest.main()