import time
import subprocess


def save_plot(fig, filename, format="png", dpi=300):

    fig.savefig(f"{filename}.{format}", format=format, dpi=dpi)
    print(f"Plot saved as {filename}.{format}")


def convert_notebook_to_script(notebook_path):
    """Convert Jupyter notebook to Python script."""

    script_path = notebook_path.replace(".ipynb", ".py")
    print(script_path)
    subprocess.run(
        ["jupyter", "nbconvert", "--to", "script", notebook_path], check=True
    )
    return script_path


def run_script(script_path):
    """Run a Python script and return the execution time."""
    start_time = time.time()
    subprocess.run(["python", script_path], check=True)
    end_time = time.time()
    return end_time - start_time
