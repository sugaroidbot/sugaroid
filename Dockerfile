FROM python:3.9-buster as base 

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



FROM base as toolbox

RUN apt-get update && apt-get install -qqy vim zsh



FROM base

# Creating folders, and files for a project:
COPY . /code

EXPOSE 5000

ENTRYPOINT ["python3", "-m", "sugaroid.server"]

