"""
Corey Schafer: https://www.youtube.com/watch?v=-ARI4Cz-awo&t=0s , https://www.youtube.com/watch?v=jxmzY9soFXg&t=13s
LogRecordAttributes: https://docs.python.org/3/library/logging.html#logrecord-attributes
"""

import logging
import employee

# Only one logger config can be set once a software is run
# If a logger doesn't have a config, it'll fall back to the config of root logger

# change logging level
# logging.basicConfig(filename='sample.log',
#                     level=logging.DEBUG, format='%(levelname)s:%(name)s:%(asctime)s::%(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('sample.log')

# set level on the file handler themselves
file_handler.setLevel(logging.ERROR)

file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)  # ERRORs are logged into the file
logger.addHandler(stream_handler)  # All other logs are printed to console


def add(x, y):
    """Add function"""
    return x + y


def subtract(x, y):
    """Subtract function"""
    return x - y


def multiply(x, y):
    """Multiply function"""
    return x * y


def divide(x, y):
    """Divide function"""
    try:
        result = x/y
    except ZeroDivisionError:
        # logger.error('Divide by zero not allowd')
        logger.exception('Divide by zero not allowd')
    else:
        return x / y


num_1 = 20
num_2 = 0

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

subtract_result = subtract(num_1, num_2)
logger.debug('Add: {} - {} = {}'.format(num_1, num_2, subtract_result))

multiply_result = multiply(num_1, num_2)
logger.debug('Add: {} * {} = {}'.format(num_1, num_2, multiply_result))

divide_result = divide(num_1, num_2)
logger.debug('Add: {} / {} = {}'.format(num_1, num_2, divide_result))
