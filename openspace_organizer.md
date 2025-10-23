# Challenge: Open Space Organizer

- Repository: `openspace-organizer`
- Type of Challenge: `Consolidation`
- Team challenge : `Solo`
- Duration: `2 days`
- Deadline: `24/10/25 4:00 PM`
- Show and tell: `24/10/25 4:00 - 5:00 PM` (3 randomly selected learners will present their solutions)

## Mission objectives

Create an algorithm that randomly assigns people to a spot in the openspace.

![Musical Chairs!](https://i.gifer.com/8OFn.gif)

## Learning Objectives

- Make a good usage of functions and classes.
- Use Object-Oriented-Programming (OOP).
- Use imports in a clean way.
- Use a clean architecture.
- Read data from a .txt file
- Structure a project and practice using Github.


## The Mission

Your company moved to a new office. It's an openspace with 6 tables of 4 seats. As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues.

You will create a program that runs everyday to re-assign everybody to a new seat. 

### Must-have features

You want to build a program that allows you to get a list of colleagues from an text file and place them ***randomly*** on the different tables of the open space.

#### the default setup of the open space is 6 tables of 4 seats → 24 seats ####

- The program can take a filepath as an argument to load the list of colleagues. 
- The program distributes randomly the people on the existing tables and says how much seats are left.
- The program can deal with the possibility of having to much people in the room.


### Steps

It goes without saying, but please, **read through all of this before starting.**

Make sure that you understand the concept of OOP, as this project will make intensive use of it.


_How to program a python project ?_
Until now, you've mostly been working on `.ipynb` files, so called _Jupyter Notebooks_ or `IPython notebooks`.
For a project like this, notebooks are really not a good idea. You'll notice the `.py` file extension in the coming files. These are **python** source files. Unlike notebooks, which get read using `jupyter` or `jupyter-lab`,
editing python source files is done in an [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) or a text editor.

Now, let's get to the heart of it! And I repeat, **read through all of this before starting.** We will build our functionality incrementally!

#### 0. Preparation

Create a GitHub repo called `challenge-openspace-classifier` and clone it. In this repository create 3 "empty" files:

- `README.md` : This is the document anyone looking at your portfolio will read to understand your project. We have provided a sample you can use for inspiration.
- `main.py`: Here we will have the code to run all the functionality of you program
- `dev_notebook.ipynb`: You will use this as a first step to build and test your code logic before jumping into OOP! We have provided a sample. 

And a folder, that contains all the helper modules you will build:

- `utils`

In the `utils` folder create 3 files:

- `file_utils.py`:
- `table.py`
- `openspace.py`

You're ready to go! 

#### 1. Create a first version of the project in a your development notebook

Here is a [guide](sample_dev_notebook.ipynb)! Add it to your repo and follow the steps. You will create three objects a seat, a table (made of seats), and an open space (made of tables).


#### 2. Transform it into a script!
To keep the script more modular we've added an extra challenge! Now the you have tested you code in your notebook,  we will split it in different `.py` files.

In `table.py`: Add the Seat and Table classes you've created.
In `openspace.py`:  Add the Openspace class you've created and import your Seat and Table classes from your `table.py`
In `main.py`:
- Import everything you need to launch the organizer
- load the colleagues from the excel file defined in the config file
- Launch the organizer. Display the results

Voila! You have your first program. 

### Constraints

#### Imports

```python
# You CAN'T import like this:
import whatever_file
# You CAN'T import like this:
import .whatever_file
# You CAN'T import like this:
from .whatever_file.whatever_function
# You CAN'T import like this:
from .whatever_function
# You CAN'T import like this:
from whatever_file
```

```python
# You CAN import like this:
from whatever_file import whatever_function_or_class
```
Read more about imports: [Python Imports](https://csatlas.com/python-import-file-module/)
#### Code style

- Each **class** should have a [`__str__()` method](https://medium.com/swlh/understanding-repr-and-str-in-python-65dd41538943).
- Each **function or class** has to be **typed**
- Each **function or class** has to contain a **docstring** formatted like this:

```python
def add(number_one: int, number_two: int) -> int:
    """
    Function that will perform the add operation between two numbers (in params).

    :param number_one: An int that will be added to the second parameter.
    :param number_two: An int that will be added to the fist parameter.
    :return: An int that is the result of the two params being added to each other.
    """
    result = number_one + number_two
    return result
```

- Your code should be **formatted** with [black](https://pypi.org/project/black/).
- Your code should be **commented**.
- Your code should be **cleaned of any commented unused code**.

#### Repo

- Your repo should only contain the files specified.
- Your README should be nice and complete (see the #Deliverables section below). Feel free to add more information.

Please keep the must-have version separate from the nice-to-have version by using a different branch on GitHub. Please specify that in your README too.

## Deliverables

1. Publish your source code on the GitHub repository.
2. Pimp up the README file:
   - Description
   - Installation
   - Usage
   - (Visuals)
   - (Contributors)
   - (Timeline)
   - (Personal situation)

### Nice-to-have features

Now you have a basic working program but you want to make it more interactive and more configurable.

- Allow the possibility to define the room setup from a config.json file. Allow the possibility to change dynamically the setup and re-run the program.
- Make the program more dynamic and interactive by adding the possibilty to add someone in the room (a new colleague arriving or someone being late) and the possibilty to add a table if the room is full.
- Improve the algorithm to avoid having someone alone at a table
- Allow the possibility of which list (or black list) in the excel file → _X wants to be seated beside Y_ or _X doesn't want to be seated beside Y_
- Allow the possibility to ask : 
  - how much seats are in the room
  - how much people are in the room
  - how much seats are left


## Evaluation criteria

| Criteria       | Indicator                                                    | Yes/No |
| -------------- | ------------------------------------------------------------ | ------ |
| 1. Is complete | The student has realized all must-have features.             |        |
|                | There is a published GitHub repo available.                  |        |
|                | The program runs until the end without any error.               |        |
|                | The program starts by running `python main.py` in the terminal. |        |
| 2. Is correct  | The code is well typed.                                      |        |
|                | There is a docstring for every function/method/class.        |        |
|                | All the constraints are respected.                           |        |
| 3. Is great    | There is an interaction with the user.                       |        |
|                | The algorithm doesn't create table with alone people.                    |        |
|                | The result is nicely displayed and can be saved in a file. |     |
|                | The program has been developed has a team using proper git flow and management system

## Final note

![You've got this!](https://media.giphy.com/media/BcCoMy2A0eYELrRZ6O/giphy.gif)
