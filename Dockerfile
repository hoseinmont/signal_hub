FROM python:3.13-bookworm
LABEL authors="hoseinmont"

ENV VARIABLE_NAME app
ENV MODULE_NAME app
ENV APP_MODULE app:app
ENV TZ=Asia/Tehran
ENV PYTHONPATH: "${PYTHONPATH}:$(pwd)"

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /app

CMD ["fastapi", "run", "/app/app.py", "--port", "80"]
