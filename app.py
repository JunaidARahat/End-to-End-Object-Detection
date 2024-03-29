from signLanguage.logger import logging
# logging.info("welcome to the my firstlog")
from signLanguage.exception import SignException

import sys

try:

    a=7/'9'

except Exception as e:
    raise SignException(e,sys)
 