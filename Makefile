help:
	@echo "help"
init:
	@pipenv install --dev
check:
	@PIPENV_IGNORE_VIRTUALENVS=1 pipenv run flake8 app/
test:
	@echo "will be added"
build:
	@echo "will"
run:
	@PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -m app