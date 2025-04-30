import logging
import os
from datetime import datetime

def get_logger(name):
    # Create "logs" folder if not exists
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Dynamic log filename based on timestamp
    log_filename = os.path.join("logs", f"test_log_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log")

    # Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Capture all levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

    # Create handlers
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(log_filename)

    # Set level for handlers
    console_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)

    # Create formatter and add to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger