# Handlers are responsible for dispatching appropriate log messages to the handler specific destination.
import logging

logger = logging.getLogger(__name__)

# create handler.
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('./python-logging/LogFile.log')

# set level and format
stream_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.ERROR)

log_formatter = logging.Formatter('%(name)s - [ %(levelname)s ] %(message)s')

# set formatter to handler
stream_handler.setFormatter(log_formatter)
file_handler.setFormatter(log_formatter)

# add handler to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.debug("This is a debug message from log handler...")
logger.warning("This is a warning message from log handler...")
logger.error("This is a error message from log handler...")
logger.critical("This is a error message from log handler...")