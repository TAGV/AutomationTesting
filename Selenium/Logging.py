import logging

#Storing the logs in a file
logging.basicConfig(filename="test.log",
                    format="%(asctime)s:%(levelname)s:%(message)s:[%(lineno)d]:%(pathname)s",
                    datefmt="%m/%d/%Y %I: %M: %S %p")

#Creating a logging object
logger = logging.getLogger()

#Setting level to debug, to print debug and info msgs
logger.setLevel(logging.DEBUG)

#Less critical logs
logger.debug("This is debug msg!!!")
logger.info("This is info msg!!!")

#More critical logs
logger.warning("This is warning msg!!!")
logger.error("This is error msg!!!")
logger.critical("This is critical msg!!!")

