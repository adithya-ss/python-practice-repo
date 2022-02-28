import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Roll over after 5KB and keep backup logs.
# Backup format: demoLog.log.1 demoLog.log.2 etc.
log_handler = RotatingFileHandler('./python-logging/demoLog.log', maxBytes=5000, backupCount=3)
logger.addHandler(log_handler)

for _ in range(10000):
    logger.info("This is just informational. Nothing important here...")