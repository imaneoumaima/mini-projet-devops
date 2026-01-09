import logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig(
    filename='/var/log/library.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

@app.route('/library')
def get_books():
    print("Library service called")
    logging.info("Library service called")
    return {"books": ["Book A", "Book B", "Book C"]}

if __name__ == '__main__':
    print("library service running")
    logging.info("Library service running")
    app.run(host='0.0.0.0', port=5005)
