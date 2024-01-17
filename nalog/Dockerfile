FROM python:3.11-slim

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip install --upgrade pip \
    && python -m pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --without dev

COPY ./nalog .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "/app/entrypoint.sh"]
