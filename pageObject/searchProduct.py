from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

from pageObject.baseClass import BaseClass


class SearchProduct(BaseClass):
    def __init__(self, driver):
        self.driver = driver


    productType = (By.CSS_SELECTOR, "input[title='Search for products, brands and more']")
    search = (By.CSS_SELECTOR, "svg[viewBox='0 0 17 18']")
    produc = (By.XPATH, "//div[@class='_4rR01T']")


    def product_type(self):
        return self.driver.find_element(*SearchProduct.productType)

    def search_product(self):
        return self.driver.find_element(*SearchProduct.search)

    def product(self):
        return self.driver.find_element(*SearchProduct.produc)