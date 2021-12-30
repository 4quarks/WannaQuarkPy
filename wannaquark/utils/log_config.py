# coding=utf-8

import logging.config
from wannaquark.utils.constants import Constants
from datetime import datetime, timedelta


def get_date():
    # Since the backups are done at 2 am, we need to subtract one day
    date = datetime.today() - timedelta(days=1)
    date = date.strftime('%Y%m%d')
    return date


def init_logging():
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(filename=Constants.LOG_FILE, filemode='a', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')