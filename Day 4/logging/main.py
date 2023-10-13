# Basic logger
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(name)s %(levelname)s %(message)s',
    datefmt='%Y.%m.%d %H:%M:%S',
    filename='logs.log'
)

logging.debug("Debug")
logging.info("Info")
logging.warning("Warning")
logging.error("Erorr")
logging.critical("Critical")
