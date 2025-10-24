# Seat class
class Seat:
    def __init__(self) -> None:
        """
        Initialize a Seat object. By default, the seat is free and has no occupant.

        """
        self.free = True
        self.occupant = ""

    # Method to assign an occupant to a seat
    def set_occupant(self, name) -> None:
        """
        This method assigns an occupant to a seat if it is free.
        :param name: Name of the occupant.
        :return: None

        """
        if self.free == True:
            self.occupant = name
            self.free = False
            
        else:
            print("The seat is already occupied")

    # Method to remove an occupant and display it's name
    def remove_occupant(self) -> str:
        """
        This method removes the occupant from the seat if it is occupied.
        :return: Name of the removed occupant, or empty string if seat was already empty.

        """
        if self.free == False:
            previous_occupant = (
                self.occupant
            )  # Store the current occupant so we can return or display it after removing
            self.occupant = ""
            self.free = True
            print(f"The removed occupant is: {previous_occupant}")
        else:
            print("The seat is already empty")

    def __str__(self) -> str:
        """
        This method returns the name of the occupant, or 'Empty' if the seat is free.
        :return: str

        """
        return self.occupant if not self.free else "Empty"


# Table class
class Table:
    def __init__(self, table_id, capacity: int) -> None:
        """
        This method initializes a Table with a given table ID and capacity.
        :param table_id: Unique identifier for the table.
        :param capacity: Number of seats at the table. Default is 4.

        """
        self.capacity = 4
        self.table_id = table_id
        self.seats = [
            Seat() for i in range(self.capacity)
        ]  # makes one Seat() for each seat position, based on table capacity

    def has_free_spot(self) -> bool:
        """
        This method checks if the table has at least one free seat.
        :return: True if at least one seat is free, False otherwise.

        """
        for seat in self.seats:  # looks at each Seat object in the table
            if seat.free:
                
                return True
        
        return False

    def assign_seat(self, name) -> bool:
        """
        This method assigns an occupant to the first available seat.
        :param name: Name of the occupant to assign.
        :return: True if the assignment was successful, False if the table is full.

        """
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        
        return False

    def left_capacity(self) -> int:
        """
        Count the number of free seats left at the table.
        :return: Number of free seats.

        """
        count = 0  # start with zero free seats
        for seat in self.seats:  # goes through every Seat object in the table
            if seat.free:
                count += 1  # adds 1 to the count variable for every free seat found.
        
        return count  # gives back the total number of free seats

    def __str__(self) -> str:
        """
        This method returns a string representation of the table and its occupants.
        :return: A string like "Table 1: Alice, Bob" or "Table 1: Empty".

        """
        # 'occupants' - creates a list of occupant names for all seats that are not free
        # The str(seat) calls the __str__ method of Seat, which returns the occupant's name or "Empty"
        occupants = [str(seat) for seat in self.seats if not seat.free]
        if occupants:
            # Return a string showing the table ID and the names of the occupants, separated by commas.
            return f"Table {self.table_id}: {', '.join(occupants)}"
        else:
            # If no seats are occupied, returns a string indicating the table is empty.
            return "Table {self.table_id}: Empty"
