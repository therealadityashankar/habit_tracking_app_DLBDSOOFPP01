# The Habit Tracking app 📅
This is a display of a sample habit tracking application

![Person pointing at a calender](/calender_person.jpg)

## Installation and setup

This code requires the installation of python 3.11.5 or later, 
python setup instructions can be found at https://www.python.org/ for your operating system

this codebase uses no external libraries

## Usage Guidelines

### Direct usage guidelines

1. Usage of the app is extremely simple, and it can directly be used via calling `python main.py`
2. Since the app has no external dependencies, no pip installation is required (only python libraries are used here!)

### Usage Examples can be found in /examples, 5 usage examples are given below

- [weekly task 1, Cooking an Amazing meal for myself every week](/examples/cook-an-amazing-meal.md)
- [weekly task 2, Watering the cactus](/examples/watering-the-cactus.md)
- [daily task 1, Meditation](/examples/meditation.md)
- [daily task 2, Brushing my teeth](/examples/brushing-teeth.md)
- [daily task 3, Going for a morning walk](/examples/going-for-a-morning-walk.md)

## Development or Testing guidelines

- The project currently uses the [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) documentation style
- This project uses [unittest](https://docs.python.org/3/library/unittest.html) for testing, and requires no additional libraries
    + testing can simply be done using ` python -m unittest discover .\tests\ "test_*.py"`