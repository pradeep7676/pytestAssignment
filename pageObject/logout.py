from selenium.webdriver.common.by import By

from pageObject.baseClass import BaseClass


class LogoutPage(BaseClass):
    logOption = (By.XPATH, "//div[@class='_28p97w']")
    clickLogout = (By.XPATH, "//div[contains(text(),'Logout')]")

    def __init__(self, driver):
        self.driver = driver

    def log_option(self):
        return self.driver.find_element(*LogoutPage.logOption)

    def clicK_logout(self):
        return self.driver.find_element(*LogoutPage.clickLogout)
