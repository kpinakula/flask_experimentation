FROM python:3.11.2
RUN pip install poetry
WORKDIR /src
COPY pyproject.toml ./
COPY flask_api flask_api
RUN poetry install

WORKDIR /src/flask_api
EXPOSE 5000
CMD ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]
