import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a csv file and return a pandas dataframe

    Args:
        :param path (str): path to csv file

    Returns:
        pd.DataFrame: dataframe of csv file

    Exceptions:
        FileNotFoundError: if failed to load csv file
    """
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f'Failed to load csv file: {e}')
        return None
