from flask import Flask, request
from datetime import datetime
import socket
app = Flask(__name__)

@app.route('/')
def home():
    server_ip = request.host_url
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <html>
        <body>
            <h1>Name: Nermine Bacha</h1>
            <h2>Project Name: Kubernetes-bachbouchaa</h2>
            <h3>Version: V1</h3>
            <p>Server Hostname: {server_ip}</p>
            <p>Current Date: {current_date}</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


