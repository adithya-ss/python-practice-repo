import time
import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# When values - s for seconds, m for minutes, h for hours, d for days, midnight, w0 for monday, w1 for tuesday etc.
log_handler = TimedRotatingFileHandler('./python-logging/timed_rotate.log', when='s', interval=5, backupCount=3)
logger.addHandler(log_handler)

for _ in range(10):
    logger.info("This is just informational. Nothing important here...")
    time.sleep(5)