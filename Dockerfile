FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./app /app
COPY ./requirements.txt /app/

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt