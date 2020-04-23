FROM python:3.8-alpine3.11
RUN apk add gcc curl git make musl-dev linux-headers
WORKDIR /data
COPY . /data
RUN pip install --no-cache-dir -r /data/requirements.txt
CMD ["uvicorn", "websocket_app.asgi:application", "--host", "0.0.0.0", "--port", "9000"]

