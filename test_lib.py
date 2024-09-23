import pytest
from unittest import mock
from matplotlib import pyplot as plt
import os
from lib.helper import save_plot, convert_notebook_to_script, run_script


def test_save_plot():

    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])

    filename = "test_plot"
    format = "png"
    try:
        save_plot(fig, filename, format=format)
    except Exception as e:
        pytest.fail(f"save_plot raised an exception: {e}")

    assert os.path.exists(f"{filename}.{format}")

    os.remove(f"{filename}.{format}")


@mock.patch("subprocess.run")
def test_convert_notebook_to_script(mock_subprocess_run):
    mock_subprocess_run.return_value = None
    notebook_path = "test_notebook.ipynb"

    try:
        script_path = convert_notebook_to_script(notebook_path)
    except Exception as e:
        pytest.fail(f"convert_notebook_to_script raised an exception: {e}")

    assert script_path == notebook_path.replace(".ipynb", ".py")


@mock.patch("subprocess.run")
def test_run_script(mock_subprocess_run):
    mock_subprocess_run.return_value = None
    script_path = "test_script.py"

    try:
        execution_time = run_script(script_path)
    except Exception as e:
        pytest.fail(f"run_script raised an exception: {e}")

    assert execution_time >= 0


if __name__ == "__main__":
    pytest.main()
