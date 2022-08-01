from selenium.webdriver.common.by import By
from pageObject.baseClass import BaseClass

class RemoveCart(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    removing = (By.XPATH, "//div[contains(text(),'Remove')]")
    confirmation = (By.XPATH,"//div[@class='_3dsJAO _24d-qY FhkMJZ']")

    def remove_cart(self):
        return self.driver.find_element(*RemoveCart.removing)

    def remove_confirmation(self):
        return self.driver.find_element(*RemoveCart.confirmation)
