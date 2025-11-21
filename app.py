from flask import Flask
from flask import request
import logging

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, DevOps!"

@app.route('/health')
def health():
    return{"status": "up"}, 200

logging.basicConfig(filename="app.log", level=logging.INFO)

@app.before_request
def log_request():
    logging.info(f"Request: {request.method} {request.path}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

