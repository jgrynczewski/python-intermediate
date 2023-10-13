# Wczytywanie konfiguracji z pliku (ini, yaml też jest obsługiwany)
import logging

import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('CustomLogger')

logging.debug('Debug message')
