FROM python:3.8-slim


COPY Pipfile Pipfile.lock ./
RUN pip install --no-cache-dir pipenv
RUN pipenv install --system --deploy --clear

WORKDIR /app

COPY app ./app
EXPOSE 8080

CMD [ "python3", "-m" , "flask", "run"]