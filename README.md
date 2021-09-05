# Python Page Object Model Framework from Scratch

## Prerequisites
Python3 with pipenv

## To Run
* Clone repo
* Open terminal and cd to repo
* pipenv install
* pipenv shell
* cd to any day's directory
* Run tests.py or python -m unittest

day0 - Baby Steps 

1. create chrome driver using ChromeDriverManager
2. open an url
3. find element pass value to the element and select element
4. quit driver 

day1 - Implement initial POM
1. create a file with pages classes
2. each pages class contains the locators of the page and functions for each action done on the page
3. test file imported the pages class and called the functions from there

day2 - Separate pages for POM, tests structured in a class
1. create seperate directories for pages and tests
2. create separate page class files for each page class
3. each sub page classes inherits basepage class
4. test file imports sub page classes and used the functions from there

day3 - Implement unittest
1. implement test template class with setup and teardown methods
2. test class inherits test template class

day4 - Separate locators, add Explicit Wait in basepage class

day5 - Move reusable test functions to Page Objects 

day6 - Generate HTML reports 

day7 - Use configparser to read properties file 

day8 - Use Behave

day9 - Use pytest
1. Add `conftest.py`
2. Added `driver_init(request)` for class setup and teardown