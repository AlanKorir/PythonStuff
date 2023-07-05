import logging
import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleExample')
logger.debug('this is a debug message')
# logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%m/%d/%Y %H:%M:%S')

# import helperlogging

# logging.debug("A debug message")
# logging.info("An info message")
# logging.warning("A warning message")
# logging.error("An error message")
# logging.critical("A critical message")

#creating log handlers

# logger1 = logging.getLogger(__name__)

# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')

#set level and format

# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter1 = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter1)
# file_h.setFormatter(formatter1)

# logger1.addHandler(stream_h)
# logger1.addHandler(file_h)

# logger1.warning('This is a warning')
# logger1.error('This is an error')


