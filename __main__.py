import time
import os
from datetime import date

from check_to_run import get_value, get_new_batch, run_cleanup
from create_logger import create_logger
from config_parser import get_config


def checker(last_ct, logger):
    time.sleep(900)
    ct = get_value(logger)
    if ct == last_ct:
        run_cleanup(logger)
        get_new_batch(logger)
    else:
        checker(ct, logger)


if __name__ == '__main__':
    config = get_config()
    logger = create_logger(os.path.join(config.get('LOGGING', 'LOGGING_PATH'), f'{date.today()}.log'),
                           __file__,
                           config.get('LOGGING', 'LOGGING_LEVEL'))
    ct = get_value(logger)
    checker(ct, logger)
