import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:
    def wait_explicit(self, path):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(path))