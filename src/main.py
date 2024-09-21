"""
This module provides functions to add two arrays, create a pandas DataFrame
from arrays, and save the DataFrame to a CSV file.
"""

import pandas as pd
import numpy as np


def add_2_arr(arr1, arr2):
    """
    Adds two NumPy arrays element-wise.

    Args:
        arr1 (numpy.ndarray): The first array.
        arr2 (numpy.ndarray): The second array.

    Returns:
        numpy.ndarray: The element-wise sum of the two arrays.
    """
    return arr1 + arr2


def create_df(arr1, arr2, arr3):
    """
    Creates a pandas DataFrame from three arrays.

    Args:
        arr1 (numpy.ndarray): The first array.
        arr2 (numpy.ndarray): The second array.
        arr3 (numpy.ndarray): The third array, typically the sum of arr1 and arr2.

    Returns:
        pandas.DataFrame: A DataFrame containing the three arrays as columns.
    """
    return pd.DataFrame({"Array 1": arr1, "Array 2": arr2, "Array 3": arr3})


def df_to_csv(dataframe, filename):
    """
    Saves a pandas DataFrame to a CSV file.

    Args:
        dataframe (pandas.DataFrame): The DataFrame to save.
        filename (str): The name of the output CSV file.

    Returns:
        str: The name of the file where the DataFrame was saved.
    """
    dataframe.to_csv(filename, index=False)
    return filename


if __name__ == "__main__":
    first_arr = np.array([1, 2, 3])
    second_arr = np.array([4, 5, 6])

    third_arr = add_2_arr(first_arr, second_arr)

    df = create_df(first_arr, second_arr, third_arr)

    OUTPUT_FILE = df_to_csv(df, "testfile.csv")

    print(f"DataFrame saved to {OUTPUT_FILE}")
