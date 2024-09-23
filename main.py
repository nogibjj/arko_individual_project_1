import os
from lib.helper import convert_notebook_to_script, run_script


def compare_notebooks(notebook1, notebook2):
    """Compare the runtimes of two Jupyter notebooks."""
    script1 = convert_notebook_to_script(notebook1)
    script2 = convert_notebook_to_script(notebook2)

    runtime1 = run_script(script1)
    runtime2 = run_script(script2)

    print(f"Runtime of {notebook1}: {runtime1:.2f} seconds")
    print(f"Runtime of {notebook2}: {runtime2:.2f} seconds")

    os.remove(script1)
    os.remove(script2)


if __name__ == "__main__":

    notebook_path1 = "rdu_weather_analytics_polars.ipynb"
    notebook_path2 = "rdu_weather_analytics_pandas.ipynb"

    compare_notebooks(notebook_path1, notebook_path2)
