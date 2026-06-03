import json
from datetime import datetime

# Logging-Excercise:

# excercise_1:
# X
# V
# X
# X
# V
# V
# X

# excercise_2:
# INFO
# ERROR
# DEBUG
# ERROR
# WARNING
# INFO

# excercise_3:
# log a:

# logger.error("User was nont abale to logged in")
# or
# logger.info('User logged in successfully')

# log b:

# logger.info('Login', email= boll(email), password= boll(password))

# log c:

# logger.error('ERROR: payment failed')

# excercise_4:

# %(asctime)s: print time
# %(levelname)s: print level INFO etc...
# %(name)s: name of the flie
# %(message)s: the clear message hopfully

# excercise_5:

import logging

logger = logging.basicConfig(level=logging.INFO, format='%(levelname)s | %(message)s')
logger = logging.getLogger(__name__)
logger.info('Application started')

# excercise_6:

def process_payment(user_id, amount):
    logger.info(f'Starting payment for user {user_id}')
    if amount <= 0:
        logger.error('ERROR: Invalid amount')
        return
    if amount > 10000:
        logger.warning('WARNING: Large transaction')
        logger.info(f'Payment of {amount} completed for user {user_id}')

# excercise_7:

logger = logging.getLogger("payments")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s")

file_handler = logging.FileHandler("app.log", encoding="utf=8")
file_handler.setFormatter(formatter)

def greet(name: str) -> str:
    logger.info("The program as started")
    if name != str(name) :
        logger.error(f"Invalid name: {name}")
        return
    print(f" Hello {name}")
    logger.info("The program shouted as loud as it can")

# greet("Yehontan")
# greet(123)

# excercise_8:

def read_config(filepath):
    logger.debug(f"filepath = {filepath}")

    try:
        with open(filepath) as f:
            data = f.read()
        logger.info("It was a success!!!")
        return data
    
    except FileNotFoundError as e:
        logger.exception(f"The error is : {e}")
        return None
    
# read_config("Manman")

# excercise_9:

def write_structured_log(message, module, level, **extra):
    time_stamp = datetime.utcnow().isoformat()

    d = {"timestamp": time_stamp,
          "level": level,
            "module": module,
              "message": message}
    
    d.update(**extra)
    
    with open(file="log.json", mode="w", encoding="utf=8") as f:
        json.dump(d, f, indent=4 )

write_structured_log("User logged in", "auth", "INFO", user_id = 42  )







# excercise_10:

# from this :

"""
logger.info('done')

logger.error('failed')

logger.info('user=%s', user_id)

"""
# to this:

"""
logger.info(" The program as finished")

logger.error(' The action has failed')

logger.info('user=%s', user_id = bool(user_id))

"""

# excercise_11:

# logger.info • אדמין נכנס למערכת הניהול
# logger.error • שירות חיצוני לא מגיב
# logger.debug • פונקציית חישוב מס החלה לרוץ
# logger.warning • תעודת SSL עומדת לפוג בעוד 7 ימים
# logger.info • הזמנה בוטלה על ידי לקוח
# logger.error • תשלום נכשל 3 פעמים ברצף








# excercise_12:

# excercise_13:

# excercise_14:


