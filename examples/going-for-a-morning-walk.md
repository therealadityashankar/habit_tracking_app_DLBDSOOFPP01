# Example : going for a morning walk (Daily habit)
# This is an example for going for a morning walk with the habit manager

### Testing Setup (optional)

Testing setup can optionally be enabled via creating a ".testmode" , I would highly recommend setting this if you are testing the application out, this file should exist by default, deleting the file would change the application to run in production mode

## Test Steps

### 1. Creating the Habit

1. (optional) If test mode is active, do set the year, month and day as 2024-04-25 to have the same output as this example

```
you're currently in test mode
-----------------------------
Enter the current year : 2024
Enter the current month : 04
Enter the current day : 30 
-----------------------------
retrieved date is 2024-04-30
```

2. select adding or marking a new habit in the next step

```
Please choose what you would like to do:
Would you like to view your current habit analytics, or would you like to edit/mark your habits?
a. View Current Habits, and their analytics
b. Add to/Update/Delete your current Habits or Mark your current habits as complete
---------------------------

Please choose an option from the above options (a or b):

choice : b
```

3. Select modifying current habits (option (b))

```
Please choose what you would like to do:

Would you like to mark existing habits as complete, or modify current habits?
a. Mark habits as complete
b. Modify current habits (Add/Modify/Delete current habits)
-------------------------

choice : b
```

4. Select "Create a new habit" to add a new habit

```
Please choose what you would like to do:

Would you like to create new habits, delete habits, or rename current habits?
a. Create a new habit
b. Rename existing habit and description
c. Delete habit
-------------------------

choice : a
```

5. Enter a appropriate name and description for the habit, to be able to set the habit up, and set it up as a daily habit

```
Enter habit name: Example Going for a morning walk
Enter a description for the habit: Example Morning walk

Would you like this task to be a daily task, or a weekly task?

a. daily
b. weekly
-------------------------

choice : a
```

### 2. Renaming the Habit

1. (optional) If test mode is active, do set the year, month and day as 2024-04-25 to have the same output as this example

```
you're currently in test mode
-----------------------------
Enter the current year : 2024
Enter the current month : 04
Enter the current day : 30 
-----------------------------
retrieved date is 2024-04-30
```

2. select adding or marking a new habit in the next step

```
Please choose what you would like to do:
Would you like to view your current habit analytics, or would you like to edit/mark your habits?
a. View Current Habits, and their analytics
b. Add to/Update/Delete your current Habits or Mark your current habits as complete
---------------------------

Please choose an option from the above options (a or b):

choice : b
```

3. Select modifying current habits (option (b))

```
Please choose what you would like to do:

Would you like to mark existing habits as complete, or modify current habits?
a. Mark habits as complete
b. Modify current habits (Add/Modify/Delete current habits)
-------------------------

choice : b
```

4. Select renaming the current habit (option b)

```
Please choose what you would like to do:

Would you like to create new habits, delete habits, or rename current habits?
a. Create a new habit
b. Rename existing habit and description
c. Delete habit
-------------------------

choice : b
```

5. Choose the correct habit to modify

```
Choose a habit to modify:
1: Watering Plants - Watering Plants in the front garden in the morning
2: Brushing Teeth - Brushing teeth in the morning
3: Making the bed - Making the bed in the morning
4: Taking the pengin to the zoo - taking the penguin to the zoo to have fun

Enter a number corresponding to the habit to modify: 2
```

6. And you can enter the habit name and description to modify in the final setting

```
Enter new habit name:
name : Example habit rename
Enter new habit description:
description : Example habit description

successfully modified!
----------------------
```

### 3. Marking the Habit

1. (optional) If test mode is active, do set the year, month and day as 2024-04-25 to have the same output as this example

```
you're currently in test mode
-----------------------------
Enter the current year : 2024
Enter the current month : 04
Enter the current day : 30 
-----------------------------
retrieved date is 2024-04-30
```

2. select adding or marking a new habit in the next step

```
Please choose what you would like to do:
Would you like to view your current habit analytics, or would you like to edit/mark your habits?
a. View Current Habits, and their analytics
b. Add to/Update/Delete your current Habits or Mark your current habits as complete
---------------------------

Please choose an option from the above options (a or b):

choice : b
```

3. Select to mark the habit as complete (option (b))

```
Please choose what you would like to do:

Would you like to mark existing habits as complete, or modify current habits?
a. Mark habits as complete
b. Modify current habits (Add/Modify/Delete current habits)
-------------------------

choice : a
```

4. Choose the habit to mark as complete

```
Choose a habit to mark as complete:
1: (daily) Watering Plants - Watering Plants in the front garden in the morning (last marked today)
2: (daily) Brushing Teeth - Brushing teeth in the morning (last marked today)
3: (daily) Making the bed - Making the bed in the morning (last marked today)
4: (daily) Example habit rename - Example habit description (last marked today)

Enter a number corresponding to the habit to mark as complete for today: 4
```

### 4. Viewing habit analytics

1. (optional) If test mode is active, do set the year, month and day as 2024-04-25 to have the same output as this example

```
you're currently in test mode
-----------------------------
Enter the current year : 2024
Enter the current month : 04
Enter the current day : 30 
-----------------------------
retrieved date is 2024-04-30
```

2. select viewing analytics in the next step

```
Please choose what you would like to do:
Would you like to view your current habit analytics, or would you like to edit/mark your habits?
a. View Current Habits, and their analytics
b. Add to/Update/Delete your current Habits or Mark your current habits as complete
---------------------------

Please choose an option from the above options (a or b):

choice : a
```

3. you should see something similar to the next screen below

```
Cleaning the room
   Cleaning the room in the morning
   periodicity : weekly

   current streak : 2024-04-20 - 2024-04-24
   weeks complete : 1 week
   last marked 2024-04-24, streak broken!

   longest streak : 2024-04-20 - 2024-04-24
   longest streak weeks complete : 1 week


Making Coffee in the morning
   Making a cup of hot coffee in the morning
   periodicity : daily
   *no streak yet!

Checking the cat for lice
   Checking the cat's hair for lice in the morning
   periodicity : daily
   *no streak yet!

Exercise in the morning
   Daily morning exercise
   periodicity : daily
   *no streak yet!

Meditation
   meditating for an hour everyday
   periodicity : daily
   *no streak yet!

Feeding the Dog 3x a Day
   feed andi three times a day
   periodicity : daily

   current streak : 2024-04-25 - 2024-04-25
   days complete : 1 day
   last marked 2024-04-25, streak broken!

   longest streak : 2024-04-25 - 2024-04-25
   longest streak days complete : 1 day


Visit the neighbour and talk to them
   just visit hannah for a bit, and say hi
   periodicity : weekly

   current streak : 2024-04-22 - 2024-04-28
   weeks complete : 1 week
   last marked this week

   longest streak : 2024-04-22 - 2024-04-28
   longest streak weeks complete : 1 week


Example Brushing Teeth
   Example Brushing Teeth (nice)
   periodicity : daily
   *no streak yet!

Example habit rename
   Example habit description
   periodicity : daily

   current streak : 2024-04-24 - 2024-04-24
   days complete : 1 day
   last marked today

   longest streak : 2024-04-24 - 2024-04-24
   longest streak days complete : 1 day
```

### 5. Deleting the habit

1. (optional) If test mode is active, do set the year, month and day as 2024-04-25 to have the same output as this example

```
you're currently in test mode
-----------------------------
Enter the current year : 2024
Enter the current month : 04
Enter the current day : 30 
-----------------------------
retrieved date is 2024-04-30
```

2. select adding or marking a new habit in the next step

```
Please choose what you would like to do:
Would you like to view your current habit analytics, or would you like to edit/mark your habits?
a. View Current Habits, and their analytics
b. Add to/Update/Delete your current Habits or Mark your current habits as complete
---------------------------

Please choose an option from the above options (a or b):

choice : b
```

3. Select modifying current habits (option (b))

```
Please choose what you would like to do:

Would you like to mark existing habits as complete, or modify current habits?
a. Mark habits as complete
b. Modify current habits (Add/Modify/Delete current habits)
-------------------------

choice : b
```

4. Select deleting a habit

```
Please choose what you would like to do:

Would you like to create new habits, delete habits, or rename current habits?
a. Create a new habit
b. Rename existing habit and description
c. Delete habit
-------------------------

choice : c
```

5. correctly choose the habit to delete

```
choose a habit to delete
1: Watering Plants - Watering Plants in the front garden in the morning
2: Brushing Teeth - Brushing teeth in the morning
3: Making the bed - Making the bed in the morning
4: Cleaning the room - Cleaning the room in the morning
5: Making Coffee in the morning - Making a cup of hot coffee in the morning
6: Checking the cat for lice - Checking the cat's hair for lice in the morning
7: Exercise in the morning - Daily morning exercise
8: Meditation - meditating for an hour everyday
9: Feeding the Dog 3x a Day - feed andi three times a day
10: Visit the neighbour and talk to them - just visit hannah for a bit, and say hi
11: Example Brushing Teeth - Example Brushing Teeth (nice)
12: Example habit rename - Example habit description

Enter a number corresponding to the habit to delete: 12
```

done!