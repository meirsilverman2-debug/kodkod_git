import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s | %(lineno)d')

steam_handler = logging.StreamHandler()
steam_handler.setFormatter(formatter)

file_handler = logging.FileHandler("my_log.log", encoding="utf=8")
file_handler.setFormatter(formatter)

logger.addHandler(steam_handler)
logger.addHandler(file_handler)


logger.debug("NOT SHOW!")
logger.info("Application started")
logger.error("battery is off")
logger.warning("Low disk space")


try:
    2/0
except ZeroDivisionError as e:
    logger.exception(F"This is the error: {e}")

# logging.info("Application started")
# logging.error("battery is off")




