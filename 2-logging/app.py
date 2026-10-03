import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('app.log')
    ]
)



logger=logging.getLogger("ArithmeticApp")

def add(a,b):
    result=a+b
    logger.debug("Adding two numbers: %s and %s = %s", a, b,result)
    return result


def subtract(a,b):
    result=a-b
    logger.debug("Subtracting two numbers: %s and %s = %s", a, b,result)
    return result


def multiply(a,b):
    result=a*b
    logger.debug("Multiplying two numbers: %s and %s = %s", a, b,result)
    return result

def divide(a,b):
    try:
        result=a/b
        logger.debug("Dividing two numbers: %s and %s = %s", a, b,result)
        return result
    except ZeroDivisionError:
        logger.error("Division by zero is not allowed")
        return None



add(10,15)
subtract(10,15)
multiply(10,20)
divide(20,10)


