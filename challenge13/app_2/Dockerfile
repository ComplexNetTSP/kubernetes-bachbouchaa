FROM python:3.9-slim
WORKDIR /app
RUN pip install flask pymongo
LABEL version="1.1"
COPY . .
CMD ["python", "app.py"]
