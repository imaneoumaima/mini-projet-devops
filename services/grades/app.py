import logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig(
    filename='/var/log/grades.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

@app.route('/grades')
def get_grades():
    print("Grades service called")
    logging.info("Grades service called")
    return {"grades": [15, 12, 18]}

if __name__ == '__main__':
    print("grades service running")
    logging.info("Grades service running")
    app.run(host='0.0.0.0', port=5004)
