# Imported my classes directly from the utils module
from utils.openspace import (
    Openspace,
)  # used 'utils.' to direct python where to look for the file 'openspace.py'
from utils.file_utils import (
    load_new_colleagues,
)  # Function to read names from a CSV file


if __name__ == "__main__":
    # Load the list of colleague names from the CSV file
    names = load_new_colleagues()
    # Print the list of colleagues to verify it loaded correctly
    print("Colleagues list:", names)

    # Create an Openspace instance with default 6 tables and 4 seats per table
    openspace_classifier = Openspace()
    # Assign the colleagues to tables randomly
    openspace_classifier.organize(names)
    # Display the table arrangement in the terminal
    openspace_classifier.display()
    # Store the table arrangement in a CSV file
    openspace_classifier.store("Output.csv")
