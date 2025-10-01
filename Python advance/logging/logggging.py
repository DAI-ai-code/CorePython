import logging

# INFO
# DEBUG
# ERRORS
# Trace
FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(filename="demo.log" ,level=logging.DEBUG, format = FORMAT)
logging.info("This is info log")
logging.debug("This is debug log")
logging.error("Yo error log yo")


