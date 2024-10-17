#syntax=docker/dockerfile:1.4

# Versions
FROM python:3.12-slim as python_upstream

# ---------------------------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------------------------
FROM python_upstream as builder

WORKDIR /tmp
 
RUN pip install poetry
 
COPY ./pyproject.toml ./poetry.lock* /tmp/
 
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# ---------------------------------------------------------------------------------------------
# Dev
# ---------------------------------------------------------------------------------------------
FROM python_upstream as dev
 
WORKDIR /code

RUN pip install psycopg2-binary

COPY --from=builder /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

# ---------------------------------------------------------------------------------------------
# Production
# ---------------------------------------------------------------------------------------------
FROM python_upstream as production

WORKDIR /code

RUN pip install psycopg2-binary

COPY --from=builder /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]