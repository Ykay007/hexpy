import logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ROOT = "https://api.crimsonhexagon.com/api/"

ONE_MINUTE = 60
MAX_CALLS = 120


def sleep_message(until):
    pass
    # print('Rate limit reached, sleeping for {minute} seconds.'.format(
    #     minute=ONE_MINUTE))
