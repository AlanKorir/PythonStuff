import logging

logging.basicConfig(level=logging.DEBUG)

# x = 2
# logging.debug(f"the value of x is {x}")

# logging.debug('DBG')
# logging.info('INF')
# logging.warning('WRN')
# logging.error('ERR')
# logging.critical('CRT')

# logging exceptions
try:
    1/0
except ZeroDivisionError as e:
    # logging.error("ZeroDivisionError1", exc_info=True) example 1
    logging.exception("ZeroDivisionError2")

logger1 = logging.getLogger(__name__)
formatter1 = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
handler1 = logging.FileHandler('tester1.log')
handler1.setFormatter(formatter1)
logger1.addHandler(handler1)

logger1.info("test custom logger1")


