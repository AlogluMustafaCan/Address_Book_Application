PROJECT_NAME := $(shell echo $(notdir ${PWD}) | tr A-Z a-z)

help:
	@echo ${PROJECT_NAME}
	@echo
	@echo "help"
init:
	@pipenv install --dev
check:
	@PIPENV_IGNORE_VIRTUALENVS=1 pipenv run flake8 app/
test:
	@echo "will be added"
build:
	@docker build -t ${PROJECT_NAME} .
run:
	@PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -m app