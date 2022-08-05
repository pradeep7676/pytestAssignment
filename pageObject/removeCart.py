from selenium.webdriver.common.by import By
from pageObject.baseClass import BaseClass

class RemoveCart(BaseClass):

    removing = (By.XPATH, "//div[contains(text(),'Remove')]")
    confirmation = (By.XPATH, "//div[@class='_3dsJAO _24d-qY FhkMJZ']")

    def __init__(self, driver):
        self.driver = driver

    def remove_cart(self):
        return self.driver.find_element(*RemoveCart.removing)

    def remove_confirmation(self):
        return self.driver.find_element(*RemoveCart.confirmation)
