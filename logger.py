import logging

#create logger
logger = logging.getLogger("booking_logger")
logger.setLevel(logging.DEBUG)

#create file handler
file_handler = logging.filehandler("booking_app.log")
file_handler.setLevel(logging.DEBUG)

#formate loges
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)