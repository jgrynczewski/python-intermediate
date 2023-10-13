import logging
import logging.handlers

logger = logging.getLogger('custom')
logger.setLevel(logging.DEBUG)

rotate_h = logging.handlers.RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)

logger.addHandler(rotate_h)

for idx in range(10000):
    logger.info("Hello {idx}")
