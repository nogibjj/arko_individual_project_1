PYTHON=python
PIP=pip
VENV=venv
SRC=src
TEST=tests
FORMAT=black
LINT=pylint

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(VENV)/bin/$(PIP) install --upgrade $(PIP)
	$(VENV)/bin/$(PIP) install -r requirements.txt

format:
	$(VENV)/bin/$(FORMAT) $(SRC)/*.py

lint:
	$(VENV)/bin/$(LINT) $(SRC)/*.py
	

test:
	PYTHONPATH=$(SRC) $(VENV)/bin/$(PYTHON) -m unittest discover -s $(SRC)/$(TEST) -v

run:
	PYTHONPATH=$(SRC) $(VENV)/bin/$(PYTHON) $(SRC)/main.py
