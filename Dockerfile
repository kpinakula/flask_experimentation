FROM python:3.11.2
RUN pip install poetry
WORKDIR /src
COPY pyproject.toml ./
COPY flask_api flask_api
RUN poetry install

WORKDIR /src/flask_api
CMD ["poetry", "run", "flask", "run"]