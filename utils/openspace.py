# as the files are in the same folder, I dont have to indicate 'utils.table' when importing
from .table import Seat, Table
import random


class Openspace:
    """
    Class to represent an open space with multiple tables and seats,
    allowing assignment of colleagues to available seats.

    """

    def __init__(self) -> None:
        """
        Initialize the Openspace with a fixed number of tables and seats per table.

        """
        self.number_of_tables = 6
        self.seats_per_table = 4
        # Creates a list of Table objects with unique IDs and the specified capacity
        self.tables = [
            Table(table_id=i + 1, capacity=self.seats_per_table)
            for i in range(self.number_of_tables)
        ]  

    def __str__(self) -> str:
        """
        String representation of the Openspace showing all tables.

        """
        return "\n".join(str(table) for table in self.tables)

    def organize(self, names) -> None:
        """
        Assign names to available seats randomly across tables.
        :param names: List of colleague names to be assigned to seats.
        :return: None

        """
        # This code loops through all the tables to check if there are available spots
        for name in names:
            free_tables = []
            for table in self.tables:
                if table.has_free_spot():
                    # adds tables with free spots to the list 'free_tables'
                    free_tables.append(table)

            if free_tables:
                # Randomize the order of free tables
                random.shuffle(free_tables)
                chosen_table = free_tables[0]
                # Assigns the colleague to a free seat in the chosen table
                assigned = chosen_table.assign_seat(name)
            else:
                print(f"No free spots left. {name} could not be assigned a seat.")

    def display(self) -> None:
        """
        This method  prints the current state of the Openspace (all tables and occupants).

        """
        print(self)

    def store(self, filename) -> None:
        """
        Store the current state of the Openspace in a file.
        :param filename: Name of the file to write the table arrangement to.
        :return: None

        """
        # UTF-8 encoding is important so we could save the table arrangement
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(self))
            
