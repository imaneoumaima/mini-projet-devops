import logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig(
    filename='/var/log/teachers.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

@app.route('/teachers')
def get_teachers():
    print("Teachers service called")
    logging.info("Teachers service called")
    return {"teachers": ["Mr. Smith", "Ms. Johnson"]}

if __name__ == '__main__':
    print("teachers service running")
    logging.info("Teachers service running")
    app.run(host='0.0.0.0', port=5007)
