FROM python:3.9-buster

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY pyproject.toml /code
COPY poetry.lock /code

# Project initialization:
RUN pip install poetry \
  && poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /code

ENTRYPOINT ["sugaroid-ws"]
