import logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig(
    filename='/var/log/attendance.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

@app.route('/attendance')
def get_attendance():
    print("Attendance service called")
    logging.info("Attendance service called")
    return {"attendance": "Present"}

if __name__ == '__main__':
    print("attendance service running")
    logging.info("Attendance service running")
    app.run(host='0.0.0.0', port=5001)
