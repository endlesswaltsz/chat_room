FROM python:3.8
WORKDIR /data
COPY . /data
RUN pip install --no-cache-dir -r /data/requirements.txt
CMD ["uvicorn", "websocket_app.asgi:application", "--host", "0.0.0.0", "--port", "8000"]

