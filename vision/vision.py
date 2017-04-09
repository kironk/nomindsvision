import logging.config
import sys

from conf import settings
from coredata import NSE
from coredata import QuandlException

__author__ = 'Kiron Krishnankutty <kironnk@gmail.com>'
__version__ = '1.0'

logging.config.dictConfig(settings.log_config)
log = logging.getLogger('main')


def main():
    try:
        nse = NSE(settings.quandl_api_key)
        log.info(nse)
    except QuandlException as error:
        log.error(error)
        return 2


if __name__ == '__main__':
    if sys.version_info >= (3, 6, 1):
        sys.exit(main())
    else:
        log.error('Requires python 3.6.1 or above. '
                  'Please download and install the latest python 3 from '
                  'https://www.python.org/downloads.')
        sys.exit(1)
