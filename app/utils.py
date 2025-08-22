import logging

def configure_logging() -> logging.Logger:
    logger = logging.getLogger("ml-service")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(message)s')  # raw JSON string
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger