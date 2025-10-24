import pandas as pd
from pathlib import Path  # to make it easier to work with file paths and files


def load_new_colleagues() -> list[str]:
    """
    This method loads the list of new colleagues from a CSV file in the project root.
    :raises FileNotFoundError: If the CSV file does not exist.
    :return: A list of names (strings) from the CSV file.

    """
    # Path to the csv file in the project root
    csv_path = Path(__file__).parent.parent / "new_colleagues.csv"

    # Checks if csv file actually exists
    if not csv_path.exists():
        raise FileNotFoundError(f"{csv_path} does not exist!")

    # Reads the CSV file into a pandas DataFrame, without using a header row
    df = pd.read_csv(csv_path, header=None)

    # 'tolist' - to convert pandas series  into a regular Python list
    return df[0].tolist()
