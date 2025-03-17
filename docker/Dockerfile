FROM python:3.12

RUN  pip install poetry==2.1.1

RUN mkdir /app
COPY ./poetry.lock ./pyproject.toml /app/

WORKDIR /app/
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
