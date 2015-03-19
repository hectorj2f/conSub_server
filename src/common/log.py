import logging
import sys

from common import resources
from common.config import settings

logger = logging.getLogger(resources.CONSUB_LOGNAME)

if 'debug' in settings['debug']['mode']:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)
