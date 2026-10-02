from logger import logging


def add(a,b):
    logging.debug("Adding two numbers: %s and %s", a, b)
    return a+b

logging.debug("Addition function is called")
add(10,15)
