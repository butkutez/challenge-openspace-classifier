# OpenSpace Organizer
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## Description

Your company moved to a new office at CEVI Ghent. Its an openspace with 6 tables of 4 seats. As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues. 

This script runs everyday to re-assign everybody to a new seat.

[![coworking img](https://assets.weforum.org/article/image/b1_5XLY0n3MmDU4hETTHgkGd7zvtIrvxcK7151Myj2s.jpg)](https://www.weforum.org/stories/2021/12/5-key-insights-on-the-future-readiness-of-smes/)

*Image source: [World Economic Forum](https://www.weforum.org/stories/2021/12/5-key-insights-on-the-future-readiness-of-smes/)*

## Repo structure

```
.
├── utils/
│   ├── __init__.py
│   ├── file_utils.py
│   ├── openspace.py
│   └── table.py
├── .gitignore
├── main.py
├── new_colleagues.csv
├── README.md
└── Output.csv
```
## Installation

1. **Clone the project:**

- git clone <repository-url>
- cd <project-folder>

2. **Install dependencies (OPTIONAL):**

- npm install
- yarn install

3. **clear structure** they can adapt for any project:

1. Clone → navigate  
2. Install dependencies  
3. Run or build (npm start) 


## Usage

1. Clone the repository to your local machine (see section: Installation).

2. To run the script, you can execute the `main.py` file from your command line:

```
   python main.py
```

3. The script reads your input file (new_colleagues.csv), and organizes your colleagues to random seat assignments. The resulting seating plan is displayed in your console and also saved to an "Output.csv" file in your root directory. 

```python

from utils.openspace import Openspace
from utils.file_utils import load_new_colleagues

def main():

    # Load the list of colleagues from the CSV file
    names = load_new_colleagues()

    # Create an Openspace instance
    openspace_classifier = Openspace()

    # Randomly assign colleagues to tables
    openspace_classifier.organize(names)

    # Display the table arrangement
    openspace_classifier.display()

    # Save the table arrangement to an output CSV file
    openspace_classifier.store("Output.csv")

if __name__ == "__main__":
    main()

```
## Timeline

This project took two days for completion.

## Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 

Connect with me on [LinkedIn](https://www.linkedin.com/in/zivile-butkute/).

## Most IMPORTANTLY

[![gif-have-fun](https://media.tenor.com/zsU8anCyoSIAAAAM/dance-maracas.gif)](https://tenor.com/en-GB/view/dance-maracas-shake-mexican-joe-manganiello-gif-14899381370080108834)
*GIF source: [Tenor](https://tenor.com/en-GB/view/dance-maracas-shake-mexican-joe-manganiello-gif-14899381370080108834)*