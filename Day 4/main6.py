# Logowanie wyjątków
import logging


try:
    a = [1, 2, 3]
    a[5]
except IndexError as e:
    logging.error(e, exc_info=True)
