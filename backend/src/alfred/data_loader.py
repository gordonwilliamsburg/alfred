import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load data from a CSV file into a Pandas DataFrame.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data in a Pandas DataFrame.
    """
    data = pd.read_csv(filepath)
    return data
