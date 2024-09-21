"""
This module contains unit tests for functions in the main.py module.
"""

import os  # Standard library imports first
import sys
import unittest
from io import StringIO

import numpy as np  # Third-party imports after standard library imports
import pandas as pd
from main import add_2_arr, create_df, df_to_csv  # Local imports at the top


class Test(unittest.TestCase):
    """
    Unit test class for testing the functions in main.py.
    """

    def test_add_2_arr(self):
        """
        Tests the add_2_arr function to ensure it correctly adds two arrays.
        """
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        res_arr = np.array([5, 7, 9])
        np.testing.assert_array_equal(add_2_arr(arr1, arr2), res_arr)

    def test_create_df(self):
        """
        Tests the create_df function to ensure it creates a DataFrame correctly.
        """
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        arr3 = np.array([5, 7, 9])
        df = create_df(arr1, arr2, arr3)
        res_df = pd.DataFrame(
            {"Array 1": [1, 2, 3], "Array 2": [4, 5, 6], "Array 3": [5, 7, 9]}
        )
        pd.testing.assert_frame_equal(df, res_df)

    def test_df_to_csv(self):
        """
        Tests the df_to_csv function to ensure it correctly saves a DataFrame to CSV format.
        """
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        arr3 = np.array([5, 7, 9])
        df = create_df(arr1, arr2, arr3)

        # Ensuring the tests are isolated and don't depend on the filesystem.
        buffer = StringIO()
        df_to_csv(df, buffer)
        buffer.seek(0)
        res_df = pd.read_csv(buffer)

        expected_df = pd.DataFrame(
            {"Array 1": [1, 2, 3], "Array 2": [4, 5, 6], "Array 3": [5, 7, 9]}
        )

        pd.testing.assert_frame_equal(res_df, expected_df)


if __name__ == "__main__":
    # Only modify the system path when running the script directly
    sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))
    unittest.main()
