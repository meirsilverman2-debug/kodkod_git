import logging

logging.basicConfig(
    level=logging.INFO,
    format=" | %(asctime)s |%(levelname)s |%(message)s |",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log", encoding='utf-8')
    ]
)

name = "Meir"
item = 1
logging.info("my name %s and I bought %d item", name, item)# These ar place holders for the variable after the message string
logging.info("test")