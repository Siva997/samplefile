# def stars(f, *args, **kwargs):
#     print("***********")
#     ret = f(*args, **kwargs)
#     print("***********")
#     return ret
# @stars
# def add(x, y):
#     c = x + y
#     print(c)
#
# s = add(5,6)

import logging
import sys

FORMAT = '%(threadName)s %(filename)10s %(levelname)10s %(levelno)5d %(funcName)10s %(asctime)10s %(msecs)10s %(message)10s'

logging.basicConfig(level = logging.DEBUG,
                    filename = "siva.log",
                    filemode = "w",
                    format = FORMAT,
                    datefmt = "%H:%M:%S"

                    )
logger = logging.getLogger("siva_logg")
def stars(f):
    def wrapper(*args,**kwargs):
            logger.debug("***********")
            ret = f(*args, **kwargs)
            logger.debug("***********")
            return ret
    return wrapper



@stars
def add():
    logger.debug( "happy birthday")


add()






# ------------------


