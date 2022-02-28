import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s [ %(levelname)s ] %(message)s', 
datefmt='%m/%d/%Y %H:%M:%S')

logger = logging.getLogger(__name__)
# If the logging should not be propogated to base logger, then below has to be set.
# logger.propagate = False
logger.info("Hello there! This is helper.")