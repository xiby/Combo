import logging
import time
import os

def getLogger(name):
    '''
    get a logger, redirect output to file and console
    '''
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    rq = time.strftime('%Y%m%d', time.localtime(time.time()))
    log_path = os.path.split(os.path.realpath(__file__))[0] + "/../../out/"
    log_name = log_path + 'Combo-' + rq + '.log'
    logfile = log_name
    fh = logging.FileHandler(logfile, mode='a+')
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
