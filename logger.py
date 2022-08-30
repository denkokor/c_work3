import logging
from config import LOGGER_API_PATH, LOGGER_FORMAT

def config():

    api_logger = logging.getLogger("api_logger")
    api_logger.setLevel(logging.DEBUG)

    api_logger_handler = logging.FileHandler(filename=LOGGER_API_PATH)
    api_logger_handler.setLevel(logging.DEBUG)
    api_logger.addHandler(api_logger_handler)

    api_logger_format = logging.Formatter(LOGGER_FORMAT)
    api_logger_handler.setFormatter(api_logger_format)