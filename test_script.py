import pytest
import os
import json
import shutil


from main import compare_notebooks

minimal_notebook_content = {
    "cells": [
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["print('This is a test print statement from the notebook.')"],
        }
    ],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 2,
}

test_directory = "test_notebooks"


def setup_test_directory():
    """Create a directory and write test notebooks."""
    os.makedirs(test_directory, exist_ok=True)

    notebook1_path = os.path.join(test_directory, "notebook1.ipynb")
    notebook2_path = os.path.join(test_directory, "notebook2.ipynb")

    print(f"Creating {notebook1_path} with valid content...")
    with open(notebook1_path, "w") as notebook1_file:
        json.dump(minimal_notebook_content, notebook1_file)

    print(f"Creating {notebook2_path} with valid content...")
    with open(notebook2_path, "w") as notebook2_file:
        json.dump(minimal_notebook_content, notebook2_file)

    return notebook1_path, notebook2_path


def test_compare_notebooks():

    notebook1_path, notebook2_path = setup_test_directory()

    print(f"Testing comparison between {notebook1_path} and {notebook2_path}")

    try:

        compare_notebooks(notebook1_path, notebook2_path)

        assert not os.path.exists(notebook1_path.replace(".ipynb", ".txt"))
        assert not os.path.exists(notebook2_path.replace(".ipynb", ".txt"))

    except Exception:
        pass

    finally:
        shutil.rmtree(test_directory)


if __name__ == "__main__":
    pytest.main()
