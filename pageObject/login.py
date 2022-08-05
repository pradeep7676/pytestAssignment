from datetime import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from testData.testData import TestData


class LoginPage:
    un = (By.CSS_SELECTOR, "input[class='_2IX_2- VJZDxU']")
    pw = (By.XPATH, "//input[@type='password']")
    login = (By.XPATH, "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")

    def login_creditionals(self, credi):
        loginPage = LoginPage(self.driver)
        loginPage.userName().send_keys(credi['user_id'])
        loginPage.passward().send_keys(credi['passward'])
        loginPage.loginButton().click()
        log_val = self.driver.title
        assert "Online Shopping" in log_val
        return credi

    def __init__(self, driver):
        self.driver = driver

    def userName(self):
        return self.driver.find_element(*LoginPage.un)

    def passward(self):
        return self.driver.find_element(*LoginPage.pw)

    def loginButton(self):
        return self.driver.find_element(*LoginPage.login)

