from flask import Flask, request
from datetime import datetime
from pymongo import MongoClient
import socket

app = Flask(__name__)

# MongoDB configuration
client = MongoClient("mongodb://mongodb:27017/") 
db = client['kubernetes_bachbouchaa_db']  # Database name
collection = db['requests'] 

@app.route('/')
def home():
    # Get client information
    client_ip = request.remote_addr  # Get client IP address
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert data into MongoDB
    record = {
        "ip_address": client_ip,
        "date": current_date
    }
    collection.insert_one(record)  # Save record to MongoDB

    # Fetch the last 10 records from MongoDB
    last_records = collection.find().sort('_id', -1).limit(10)

    # Generate HTML response
    records_html = ""
    for record in last_records:
        records_html += f"<li>IP: {record['ip_address']} - Date: {record['date']}</li>"

    server_hostname = socket.gethostname()  # Get server hostname

    return f"""
    <html>
        <body>
            <h1>Name: Nermine Bacha</h1>
            <h2>Project Name: Kubernetes-bachbouchaa</h2>
            <h3>Version: V2</h3>
            <p>Server Hostname: {server_hostname}</p>
            <p>Current Date: {current_date}</p>
            <h4>Last 10 Records:</h4>
            <ul>
                {records_html}
            </ul>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


