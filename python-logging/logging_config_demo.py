import logging
import logging.config

logging.config.fileConfig('./python-logging/logging.conf')

logger = logging.getLogger('anotherDemo')
logger.debug('This is another debug message...')