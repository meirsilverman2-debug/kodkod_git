import logging


logging.basicConfig(
    level= logging.INFO,
    format= " %(asctime)s | %(levelname)s | %(message)s |"
)

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

format = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s |")

file_handler = logging.FileHandler("system.log")
file_handler.setFormatter(format)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(format)
logger.addHandler(stream_handler)


logger.info("testing the logger")