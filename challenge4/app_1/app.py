from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <html>
        <body>
            <h1>Flask App without Database</h1>
            <p>Server: {socket.gethostname()}</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
