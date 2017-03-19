import time


def get_time():
    localtime = time.strftime("%Y%m%d_%H%M", time.localtime())
    return localtime
