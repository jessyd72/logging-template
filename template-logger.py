'''
12/2022
This is a template for contructing a simple logger that writes
to a log file and prints to the current instance (Stream).
    - Level set to INFO
    - File and Stream Handler set

Logging documentation- https://docs.python.org/3/library/logging.html

'''

import logging 
import os
import sys
import datetime


# set paths
home_fldr = os.path.dirname(__file__)
log_fldr = os.path.join(home_fldr, "logs")

# get today
timestamp = datetime.datetime.today().strftime("%Y%m%d")

# set logging
log_file = os.path.join(log_fldr, f"task_log_{timestamp}.log")
logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s: %(asctime)s %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    handlers=[logging.FileHandler(log_file),
                            logging.StreamHandler(sys.stdout)])

logging.info("This is an information message")
logging.warn("This is a warning message")
logging.error("This is an error message")

