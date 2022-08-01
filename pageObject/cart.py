from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.baseClass import BaseClass


class CartPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver


    productName = (By.XPATH,"//span[@class='B_NuCI']")
    productPrice = (By.XPATH, "//div[@class='_30jeq3 _16Jk6d']")
    addingCart = (By.XPATH, "//button[@class='_2KpZ6l _2U9uOA _3v1-ww']")

    def get_productName(self):
        return self.driver.find_element(*CartPage.productName)

    def get_productPrice(self):
        return self.driver.find_element(*CartPage.productPrice)

    def adding_cart(self):
        return self.driver.find_element(*CartPage.addingCart)