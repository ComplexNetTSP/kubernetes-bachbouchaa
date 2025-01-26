from flask import Flask, request
from datetime import datetime
from pymongo import MongoClient
import socket
import os

app = Flask(__name__)

# MongoDB Configuration
mongo_host = os.getenv("MONGO_HOST", "localhost")
mongo_port = os.getenv("MONGO_PORT", "27017")
mongo_uri = f"mongodb://{mongo_host}:{mongo_port}/"

client = MongoClient(mongo_uri)  # Connect to MongoDB service
db = client['webapp_db']
collection = db['requests']

@app.route('/')
def home():
    # Get client information
    client_ip = request.remote_addr
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert data into MongoDB
    record = {"ip_address": client_ip, "date": current_date}
    collection.insert_one(record)

    # Fetch the last 10 records
    records = list(collection.find().sort('_id', -1).limit(10))

    # Generate HTML
    records_html = "".join(f"<li>{r['ip_address']} - {r['date']}</li>" for r in records)
    return f"""
    <html>
        <body>
            <h1>Flask App with Database - Version 1.2 </h1>
            <h1>Name: Nermine Bacha </h1>
            <p>Server: {socket.gethostname()}</p>
            <ul>{records_html}</ul>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

