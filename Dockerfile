FROM python:3.9-alpine

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

# Copy only requirements to cache them in docker layer
WORKDIR /code

# Creating folders, and files for a project:
COPY . /code


# Project initialization:
RUN apk add --no-cache openssl-dev gcc musl-dev libffi-dev \
  && pip install poetry \
  && poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi \
  && apk del openssl-dev libffi-dev gcc musl-dev

ENTRYPOINT ["sugaroid-ws"]
