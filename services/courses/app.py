import logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig(
    filename='/var/log/courses.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

@app.route('/courses')
def get_courses():
    print("Courses service called")
    logging.info("Courses service called")
    return {"courses": ["Math", "Science", "History"]}

if __name__ == '__main__':
    print("courses service running")
    logging.info("Courses service running")
    app.run(host='0.0.0.0', port=5002)
