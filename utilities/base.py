import inspect
import logging

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class Base:

   def logging(self, message):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler('logfile.log')
        logger.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.info(message)