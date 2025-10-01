import logging

class Calculator:
    FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename='calc_logs.log', level=logging.DEBUG, filemode='a', format=FORMAT)

    def __init__(self):
        logging.info('User picked up calculator.')

    @staticmethod
    def add(a,b):
        logging.info('User wants to add.')
        return a + b

    @staticmethod
    def subtract(a,b):
        logging.info('User wants to subtract.')
        return a - b

    @staticmethod
    def multiply(a, b):
        logging.info('User wants to multiply.')
        return a*b

    @staticmethod
    def divide(a, b):
        logging.info('User wants to divide.')
        if int(b) == 0:
            logging.error('Error! User tried to divide by 0.')
            raise ZeroDivisionError
        return a / b


    @staticmethod
    def isPrime(n):
        logging.info('User wants to check if a number is prime or not.')
        for i in range(2, int(n ** 0.5) + 1):
            if n%i == 0:
                logging.debug('Control flow has entered the if condition.')
                return False
        else:
            logging.debug('Control flow has NOT entered the if condition.')
            return True


calc = Calculator()

calc.add(1, 2)
calc.subtract(1, 2)
calc.multiply(1,2)
calc.divide(1,2)
# calc.divide(1,0)
calc.isPrime(3)

