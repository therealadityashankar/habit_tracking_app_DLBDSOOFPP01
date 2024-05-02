"""
The files to test all the code in the code base

the 'mock_input' function overrides the input function in the code, 
to be able to thoroughly test the codebase

Tests to check if the "watering the cactus" habit
1. Can be added
2. Can have the name and description changed
3. Can be marked as completed for the today, and for the next 3 weeks (so maintaining a 4 week streak)
4. Can be not marked for 1 week, and thus cause a loss of a streak
5. Can be removed
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
    "test-watering-the-cactus", # the name of the habit
    "testing watering the cactus once a week", # the description of the habit
    "b", # selecting a weekly habit

    # Checking if the habit is correctly set in analytics
    "2024", "04", "25", # the mock date setup
    "a", # selecting analytics

    # 2. Renaming a habit
    "2024", "04", "25", # the mock date setup
    "b", "b", "b", # selecting creating a new habit
    str(len(habits) + 1), # selecting the newest habit,
    "test-watering-the-cactus-renamed",
    "testing watering the cactus once a week", # the description of the habit,

    # Checking if the habit is correctly renamed in analytics
    "2024", "04", "25", # the mock date setup
    "a" # selecting analytics
]

# 3. adding a week of marking to the above list, to ensure that the habit
# can be correctly marked continuously for 4 weeks
for i in range(4):
    date = datetime.date(2024, 4, 25) + datetime.timedelta(weeks=i)
    complete_test_cli_operations.extend([
        # marking the task
        str(date.year), str(date.month), str(date.day), # select the date, i.e. today, the next week or the week after next week
        "b", "a", # selecting marking a task
        str(len(habits) + 1), # selecting the task to mark
        "b", # just marking one task for now!

        # analysing if the task is correctly marked
        str(date.year), str(date.month), str(date.day), # the mock date setup
        "a", # selecting analytics
    ])

# 4. Can be not marked for 1 week, and thus cause a loss of a streak
date = date + datetime.timedelta(weeks=2)

complete_test_cli_operations.extend([
        # marking the task one day later
        str(date.year), str(date.month), str(date.day), # select the date, i.e. 2 weeks later
        "b", "a", # selecting marking a task
        str(len(habits) + 1), # selecting the task to mark
        "b", # just marking one task for now!

        # analysing if the task is correctly marked
        # and the streak has been broken
        str(date.year), str(date.month), str(date.day), # the mock date setup
        "a", # selecting analytics
])

# 5. Remove the item
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

        return test_value
    
    return real_mock_input

# Test case with custom side effect
class TestWateringCactus(unittest.TestCase):
    """

    in addition, analytics in each step above will be checked to
    ensure that each step is functioning properly
    """
    @classmethod
    def setUpClass(cls):
        """
        Create '.testmode' file if it does not exist.
        """
        cls.testmode_file = ".testmode"
        cls.testfile_existed_before = True

        if not os.path.exists(cls.testmode_file):
            cls.testfile_existed_before = False
            
            with open(cls.testmode_file, "w") as f:
                f.write("Test mode is active.")
    
    @classmethod
    def tearDownClass(cls) -> None:
        """
        and delete .testmode if the file did not exist before
        """
        with open(os.path.join(parent_directory, "data.json"), "w") as f:
            json.dump({"habits":habits}, f, indent=2)

        if os.path.exists(cls.testmode_file) and not cls.testfile_existed_before:
            os.remove(cls.testmode_file)


    def step1_habit_creation_weekly_test(self):
        """
        checks if weekly habits can be successfully added or not
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
        test-watering-the-cactus
           testing watering the cactus once a week
           periodicity : weekly
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
        test-watering-the-cactus-renamed
           testing watering the cactus once a week
           periodicity : weekly
           *no streak yet!""")

        self.assertIn(output_should_contain, output)

    def step3_habit_marking_test(self):
        """
        checks if habit has been successfully marked or not
        """
        for i in range(4):
            date = datetime.date(2024, 4, 22) + datetime.timedelta(weeks=i)
            weekend = date + datetime.timedelta(weeks=1) - datetime.timedelta(days=1)

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
            test-watering-the-cactus-renamed
               testing watering the cactus once a week
               periodicity : weekly

               current streak : 2024-04-22 - 2024-{weekend.month:02d}-{weekend.day:02d}
               weeks complete : {i + 1} week{"s" if i > 0 else ""}
               last marked this week

               longest streak : 2024-04-22 - 2024-{weekend.month:02d}-{weekend.day:02d}
               longest streak weeks complete : {i + 1} week{"s" if i > 0 else ""}""")

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
        test-watering-the-cactus-renamed
           testing watering the cactus once a week
           periodicity : weekly

           current streak : 2024-05-27 - 2024-06-02
           weeks complete : 1 week
           last marked this week

           longest streak : 2024-04-22 - 2024-05-19
           longest streak weeks complete : 4 weeks""")

        self.assertIn(output_should_contain, output)
    
    def step5_habit_deletion_test(self):
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

        output_should_not_contain = textwrap.dedent(f"test-watering-the-cactus-renameds")
        self.assertNotIn(output_should_not_contain, output)
    
    @patch('builtins.input', side_effect=mock_input(complete_test_cli_operations))
    def test_watering_cactus_habit(self, mock_input):
        self.step1_habit_creation_weekly_test()
        self.step2_habit_renaming_test()
        self.step3_habit_marking_test()
        self.step4_habit_not_marking_test()
        self.step5_habit_deletion_test()
    

if __name__ == '__main__':
    unittest.main()