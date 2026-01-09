import logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig(
    filename='/var/log/frontend.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

@app.route('/')
def home():
    print("Frontend service called")
    logging.info("Frontend service called")
    return {"message": "Welcome to the frontend"}

if __name__ == '__main__':
    print("frontend service running")
    logging.info("Frontend service running")
    app.run(host='0.0.0.0', port=5003)
