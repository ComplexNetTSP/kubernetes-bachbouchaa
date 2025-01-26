FROM python:3.9-slim
WORKDIR /app
RUN pip install flask
LABEL version="1.1"
COPY . .
CMD ["python", "app.py"]
