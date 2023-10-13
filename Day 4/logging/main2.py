# Custom logger
import logging


logger = logging.getLogger('CustomLogger')
logger.setLevel(logging.DEBUG)

stream_h = logging.StreamHandler()
logger.addHandler(stream_h)

stream_f = logging.Formatter(
    '[%(asctime)s] %(name)s %(levelname)s %(message)s'
)
stream_h.formatter = stream_f

file_h = logging.FileHandler('logs2.log')
file_h.setLevel(logging.WARNING)
logger.addHandler(file_h)

logger.debug("Debug")
logger.info("Info")
logger.warning("Warning")
logger.error("Erorr")
logger.critical("Critical")
