import logging
from config import LOG_FILE, LOG_LEVEL

def setup_logger():
    """Set up and return a logger instance."""
    logger = logging.getLogger("UPS_POD_App")
    logger.setLevel(LOG_LEVEL)

    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(LOG_LEVEL)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
