import time
import logging
import logging.handlers


logger = logging.getLogger("custom")
logger.setLevel(logging.INFO)

time_h = logging.handlers.TimedRotatingFileHandler('time_log.log', when='s', interval=2, backupCount=5)
logger.addHandler(time_h)

for idx in range(50):
    logger.info(f"Hello, {idx}")
    time.sleep(0.2)
