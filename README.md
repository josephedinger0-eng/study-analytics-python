# Study Analytics Python

A Python-based study session tracker and analytics program. This project is a Python rebuild of an earlier Java Study Analytics project, created to learn Python by translating familiar programming concepts into Python and adapting the original program to Python's syntax and design patterns.

## About

Study Analytics allows users to record and analyze their study sessions through a command-line interface.

Each study session contains:

* Date
* Subject
* Topic
* Study time in minutes
* Score

The program calculates useful statistics from these sessions and saves the data between program runs.

## Features

* Add study sessions
* View all recorded sessions
* Modify existing sessions
* Delete sessions
* Validate user input
* Calculate total study time
* Calculate average scores
* Calculate study time by subject
* Calculate average score by topic
* Calculate study time by date
* Calculate the longest consecutive study streak
* Save study sessions to a CSV file
* Load saved sessions when the program starts
* Handle missing data files for first-time users

## Project Structure

```text
study-analytics-python/
│
├── main.py
├── study_session.py
├── study_analytics.py
├── study_data_manager.py
├── study_data.csv
└── README.md
```

### `main.py`

Handles the command-line interface, user input, input validation, and program flow.

### `study_session.py`

Contains the `StudySession` class, which represents an individual study session.

### `study_analytics.py`

Contains the `StudyAnalytics` class and the methods used to calculate statistics from study sessions.

### `study_data_manager.py`

Handles saving and loading study sessions using CSV files.

## Technologies

* Python 3
* Python Standard Library
* CSV
* `datetime`
* Git & GitHub
* VS Code

## What I Learned

This project was primarily a way to learn Python by rebuilding a program I had previously written in Java.

Instead of learning Python completely separately from Java, I used the original program as a reference and translated its concepts into Python. This helped me understand both the similarities and differences between the two languages.

Some of the concepts I practiced include:

* Classes and objects
* Constructors and instance attributes
* Lists and dictionaries
* Loops and conditionals
* Functions and method decomposition
* Exception handling with `try` and `except`
* File input and output
* CSV data storage
* Date handling with `datetime`
* Input validation
* Python's `match`/`case` syntax
* String formatting with f-strings
* Git and GitHub version control

I also learned that translating a program between languages is not always a one-to-one process. Some parts of the original Java design were simplified or redesigned to better fit Python. For example, utility functions for saving and loading data were implemented as module-level functions rather than putting them inside a separate manager class.

## Java → Python

Some of the concepts I translated while rebuilding the project included:

| Java                    | Python              |
| ----------------------- | ------------------- |
| `ArrayList`             | `list`              |
| `HashMap`               | `dict`              |
| `.add()`                | `.append()`         |
| `.size()`               | `len()`             |
| `this.variable`         | `self.variable`     |
| `toString()`            | `__str__()`         |
| `try/catch`             | `try/except`        |
| `switch`                | `match/case`        |
| `Map.containsKey()`     | `key in dictionary` |
| `new StudySession(...)` | `StudySession(...)` |

This comparison helped me understand Python as a language rather than simply memorizing its syntax.

## Project Development

This project started as a Java Study Analytics program and was rebuilt from the ground up in Python.

The development process included:

1. Creating the basic `StudySession` class
2. Rebuilding the analytics functionality
3. Adding input validation
4. Creating the command-line menu
5. Adding date-based functionality and study streaks
6. Adding modification and deletion
7. Implementing CSV saving and loading
8. Debugging issues caused by differences between Java and Python
9. Refactoring parts of the program to use more natural Python design

One of the main goals throughout the project was to understand *why* Python code works differently from Java code, rather than simply translating each line directly.

## Project Status

**Complete**

The core functionality of the Study Analytics program has been implemented and tested.

This project served its main purpose of helping me learn Python while adapting a program I already understood from Java.

## What This Project Represents

This project is an example of my transition from Java to Python.

Rather than starting with a completely unfamiliar program, I rebuilt a project I had already created in Java. This allowed me to focus on learning Python's syntax, standard library, data structures, and design conventions while still solving problems I understood.

The project ultimately helped me become more comfortable writing Python independently and gave me experience adapting an existing program to a different programming language.
