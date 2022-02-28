from inspect import trace
import logging
import traceback

try:
    list_a = [12,19,22,123,675]
    # Raise an index error
    value = list_a[10]
# except IndexError as inderr:
#     logging.error(inderr, exc_info=True)
except:
    logging.error("The error is %s", traceback.format_exc())