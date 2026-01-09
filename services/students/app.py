import logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig(
    filename='/var/log/students.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

@app.route('/students')
def get_students():
    print("Students service called")
    logging.info("Students service called")
    return {"students": ["Alice", "Bob", "Charlie"]}

if __name__ == '__main__':
    print("students service running")
    logging.info("Students service running")
    app.run(host='0.0.0.0', port=5006)

