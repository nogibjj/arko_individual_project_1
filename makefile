venv:
	python -m venv .venv

install: venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt

format:
	.venv/bin/black lib/*.py test*.py main.py

lint:
	.venv/bin/ruff lib/*.py test*.py main.py

test-notebook:
	.venv/bin/pytest --nbval *.ipynb

test:
	.venv/bin/python test*.py

run:
	.venv/bin/python main.py

analyze:
	.venv/bin/python generate_md.py
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		if [ -f images/plot.png ]; then git add images/plot.png; fi; \
		if [ -f Data_summary.md ]; then git add Data_summary.md; fi; \
		git commit -m "Add generated plot and report"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi


