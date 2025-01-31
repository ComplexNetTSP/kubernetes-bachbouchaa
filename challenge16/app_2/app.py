from flask import Flask, request
from datetime import datetime
from pymongo import MongoClient
import os
import socket

app = Flask(__name__)

# MongoDB Replica Set Configuration
mongo_uri = "mongodb://mongodb-0.mongodb:27017,mongodb-1.mongodb:27017,mongodb-2.mongodb:27017/?replicaSet=rs0"

try:
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    db = client['webapp_db']
    collection = db['requests']
    # Vérifier la connexion
    client.server_info()
    print("✅ Connected to MongoDB Replica Set")
except Exception as e:
    print(f"❌ Error connecting to MongoDB: {e}")

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
            <h1>Flask App with Database - Version 1.5</h1>
            <h1>Name: Nermine Bacha </h1>
            <p>Server: {socket.gethostname()}</p>
            <ul>{records_html}</ul>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
