import time
import os
from datetime import date

from check_to_run import get_value, get_new_batch, run_cleanup
from create_logger import create_logger
from config_parser import get_config


def checker(last_ct, logger):
    time.sleep(300)
    ct = get_value(logger)
    logger.info(f'got value as {ct}')
    if ct == last_ct:
        logger.info(f'values are equal, running cleanup')
        run_cleanup(logger)
        logger.info(f'getting new values')
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
