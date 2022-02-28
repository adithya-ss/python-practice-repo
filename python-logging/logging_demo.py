import logging

# By default, only levels from and above warning are printed.
# If the lower levels have to be printed, below has to be done.
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - [ %(levelname)s ] %(message)s', 
datefmt='%m/%d/%Y %H:%M:%S')

# There are 5 levels of logging available by default, through the logging module.
# 1. Debug      2. Info     3. Warning      4. Error    5. Critical

logging.debug("Debug message...")
logging.info("Informational message...")
logging.warning("Warning message...")
logging.error("Error message...")
logging.critical("Critical error message...")

# Changing logger name.
import logging_helper