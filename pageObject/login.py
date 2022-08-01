from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver


    un = (By.CSS_SELECTOR,"input[class='_2IX_2- VJZDxU']")
    pw = (By.XPATH, "//input[@type='password']")
    login = (By.XPATH, "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")


    def userName(self):
        return self.driver.find_element(*LoginPage.un)

    def passward(self):
        return self.driver.find_element(*LoginPage.pw)

    def loginButton(self):
        return self.driver.find_element(*LoginPage.login)