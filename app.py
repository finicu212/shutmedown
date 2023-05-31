## --- LOGGING ---
import sys
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("log.log"),
        logging.StreamHandler()
    ]
)

class StreamToLogger(object):
    def __init__(self, logger, level):
       self.logger = logger
       self.level = level

    def write(self, message):
        if message.rstrip() != "":
            self.logger.log(self.level, message.rstrip())

    def flush(self):
        pass

stdout_logger = logging.getLogger('STDOUT')
sys.stdout = StreamToLogger(stdout_logger, logging.INFO)

stderr_logger = logging.getLogger('STDERR')
sys.stderr = StreamToLogger(stderr_logger, logging.ERROR)


## --- Shut me down server ---

from flask import Flask, render_template
import os
import time
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    def delayed_shutdown():
        time.sleep(5)
        if os.name == 'nt':
            os.system('shutdown /s /t 1')
        else:
            os.system('shutdown -h now')

    threading.Thread(target=delayed_shutdown).start()
    return 'Shutting down...'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
