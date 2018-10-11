import logging

def setHandler():
    mylogger = logging.getLogger("root")
    mylogger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[%(levelname)s] %(asctime)s - %(filename)s:%(funcName)s[%(lineno)d] > %(message)s')

    stream_hander = logging.StreamHandler()
    stream_hander.setFormatter(formatter)
    mylogger.addHandler(stream_hander)

    #file_handler = logging.FileHandler('my.log')
    #mylogger.addHandler(file_handler)
    return mylogger

log = setHandler()
