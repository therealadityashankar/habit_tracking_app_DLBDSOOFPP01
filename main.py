import src.data as data
import src.prompts as prompts
import src.util as util
import os

def main():
    if os.path.exists(".testmode"):
        util.TEST_MODE = True
        util.TEST_CURRENT_DATE = util.ask_current_date()

    print(prompts.INTRO)

    habits_and_streaks = data.load_all_data() # load all json data

    # ask the user if they would like to view or modify their data

    option = util.input_choice(prompts.CHOICE_VIEW_OR_MODIFY) 

    if option == "a":
        print(prompts.HABITS_PRE)
        util.pretty_print_habits_and_analytics(habits_and_streaks)

    if option == "b":
        # the user chooses if they would like to mark their current habits as complete
        # or modify their current habits
        mark_or_edit_option = util.input_choice(prompts.CHOICE_MARK_OR_MODIFY)

        if mark_or_edit_option == "a":
            mark_another_option = True
            while mark_another_option:
                util.mark_habit_as_complete(habits_and_streaks)
                mark_another_option = util.input_choice(prompts.CHOICE_MARK_ANOTHER) == 'a'

        elif mark_or_edit_option == "b":
            cud_option = util.input_choice(prompts.CHOICE_CREATE_UPDATE_DELETE)

            if cud_option == "a":
                util.create_new_habit(habits_and_streaks) # create a new habit
            
            elif cud_option == "b":
                util.update_habit(habits_and_streaks) # update habit

            elif cud_option == "c":
                util.delete_habit(habits_and_streaks) # delete habit

    data.save_all_data(habits_and_streaks)
    print()

if __name__ == "__main__":
    main()