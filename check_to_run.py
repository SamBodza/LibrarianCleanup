import subprocess
from sql_connectors import connect_single
from config_parser import get_config


def get_value(logger):
    query = """
    SELECT MAX(created)
	    FROM librarian.gcs_file
	    
    """
    time = connect_single(logger, query, get=True)

    return time


def run_cleanup(logger):
    try:
        path = get_config().get('SCRIPTS','cleanup')
        cmd = f'sudo sh {path}'
        logger.info(f'running commmand {cmd}')
        _ = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    except Exception as e:
        logger.critical(f'failed to run cleanup : {e}')


def get_new_batch(logger):
    try:
        path = get_config().get('SCRIPTS','batch')
        cmd = f'sudo python3 {path}'
        logger.info(f'running commmand {cmd}')
        _ = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    except Exception as e:
        logger.critical(f'failed to get new run : {e}')

