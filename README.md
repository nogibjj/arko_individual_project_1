[![Install](https://github.com/nogibjj/arko_individual_project_1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/arko_individual_project_1/actions/workflows/install.yml)
[![Format](https://github.com/nogibjj/arko_individual_project_1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/arko_individual_project_1/actions/workflows/format.yml)
[![Lint](https://github.com/nogibjj/arko_individual_project_1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/arko_individual_project_1/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/arko_individual_project_1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/arko_individual_project_1/actions/workflows/test.yml)

# Descriptive Statistics and Runtime Comparison using Polars and Pandas

This project is to demonstrate how to perform statistical analysis using pandas and polars. We then compare runtimes of both the approaches.

## Project Function
- A `.ipynb` notebook each for polars and pandas analysis
- A `.py` script to calculate the runtimes of each of these notebooks
- A `lib` folder with `helper.py` script to host helper function.
![image](https://github.com/user-attachments/assets/14b9ebb9-3710-4051-ac0b-1d923c89b8d3)


## Project Structure

- `src/`: Contains the source code for the project.
- `tests/`: Contains the unit tests for the project.
- `requirements.txt`: Lists the Python dependencies.
- `Makefile`: Defines common tasks like installing dependencies, running tests, linting, and running docker.
- `.devcontainer/`: Contains `Dockerfile` and VS Code configuration.
- `.github/workflows/`: Contians CI/CD workflows for GitHub.

## Project Setup
### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/nogibjj/arko_individual_project_1.git
cd arko_individual_project_1
```

### 2. Run notebooks (plots saved to `plots` subfolder)

```bash
.venv/bin/python rdu_weather_analytics_pandas.ipynb
.venv/bin/python rdu_weather_analytics_pandas.ipynb
```
![image](https://github.com/user-attachments/assets/f31f7760-baff-4d1b-a77e-a70596355295)


## 3. Run `main.py` script to see runtime results of both notebooks

![image](https://github.com/user-attachments/assets/7f7cd744-0ce0-42b4-9839-ae67f3f8e4be)

As we can see. polars tends to run quicker than its equivalent implementation in pandas.


## 4. YT video link
https://youtu.be/TTSH6CPpNzY






