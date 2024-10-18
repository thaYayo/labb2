# Uppgift 1
# Skapa en decorator “log_decorator” som loggar namnet på funktionen och dess argument.
# Använd decoratern på en funktion som utför någon enkel matematik.
# Testa funktionen och se till att loggningen fungerar.

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='program.log', level=logging.DEBUG)

def log_decorator(func):
    def wrapper(*args):
        result = func()
        logging.info(f"efter func: Namn: {func.__name__} args: {args}")    
        return result
    return wrapper

@log_decorator
def enkel_matte(*args):
    return sum(args)

enkel_matte(10,20)
