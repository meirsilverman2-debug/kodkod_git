# # execrcise_1 for your first logger

# import logging

# logger = logging.getLogger(__name__)

# logging.basicConfig(level=logging.INFO, format=" %(asctime)s | %(levelname)s |" \
# "%(name)s | %(message)s")

# logger.info("Progeam start")
# print("We learn in Kodcode")
# logger.warning("Get ready")
# logger.error("you came to the shop!!!")


# Level_1:

# insted of doing this: 

# print("User logged in")

# # we are doing this:

# import logging

# logging.warning("User logged in")

# exercise_1:

# import logging

# logging.warning("Warning")
# logging.error("Error")
# logging.info("Info about the program")

# Level_2:
"""
1.DEBUG -> some data to trace and check you know
2.INFO -> about  some action in the code
3.WARNING -> something is not ideal
4.ERROR -> an error

for example:

import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")

"""
# import logging

# logging.basicConfig(level=logging.INFO)

# # execrcise_2:

# def check_age(age):
#     if age < 0:
#         logging.error(" ERROR: Age cannot be negative number!!!!")
    
#     elif age < 18:
#         logging.warning("WARNING: You are under age keep in mind!")

#     else:
#         logging.info("INFO: This is a valid age for trying the roller coaster")

# check_age(-7)
# check_age(8)
# check_age(27)

"""
import logging

# Level_3:

logger = logging.getLogger(__name__)

# for each file its own special logger
# before that we used the default logger that was provide for us if we did not define it ourselves

for example:

import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

logger.info("Application stated")

__name__ : is the corrent file we are in it you understand?!

for example

if we are running it from - users.py

so __name__ == "users"

when you define this: logger = logging.getLogger(__name__)
when the logger will be printed on screen or rather in a log file it will say
in the message  where it came from because of that.

in short it helps you to understan from where the log message has come from.

"""
# import logging

# # exercise_3:

# logger = logging.getLogger(__name__)

# logger.info("info")

# logger.error("error")

"""
# Level_4:

for example:

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


logger = logging.getLogger(__name__)

logger.info("Server started")

and for this the output will be >>

2026-05-27 12:00:00 | INFO | Server started


Meaning:

asctime == time

levelname == the level the log looks for

message == the message itself literally

the place holders are very important when you set the format of the look of the printed data the log will reprsent itself
===================================================
and it will look like these:

%(name)s == the name of the logger

%(filename)s == the name of the file

%(lineno)d == the line number

===================================================

"""
import logging

# exercise_4:

# logging.basicConfig(
#     level=logging.INFO,
#     format = "%(asctime)s | %(levelname)s | %(message)s | %(name)s | %(file)s |%(lineno)d |"
# )

# logger = logging.getLogger(__name__)

# logger.info("info message")
# logger.warning("warning message")
# logger.error("error message")

# logger.error
# logging.info("fdgfdfgthbtrf")


