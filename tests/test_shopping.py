import logging
import time

import pytest
from selenium.webdriver import ActionChains

from pageObject.baseClass import BaseClass
from pageObject.cart import CartPage
from pageObject.login import LoginPage
from pageObject.logout import LogoutPage
from pageObject.removeCart import RemoveCart
from pageObject.searchProduct import SearchProduct
from testData.testData import TestData
from utilities.base import Base


class TestShopping(Base):

    def test_login(self, getData):
        self.driver.implicitly_wait(5)
        loginPage = LoginPage(self.driver)

        #entering useraname and passwrd
        loginPage.userName().send_keys(getData['user_id'])
        loginPage.passward().send_keys(getData['passward'])
        loginPage.loginButton().click()

    def test_searchProduct(self, searchproduct):
        sp_obj = SearchProduct(self.driver)
        sp_obj.wait_explicit(sp_obj.productType)
        time.sleep(1)
        sp_obj.product_type().send_keys(searchproduct['item'])

        sp_obj.wait_explicit(sp_obj.search)
        sp_obj.search_product().click()

        sp_obj.wait_explicit(sp_obj.produc)
        sp_obj.product().click()

    def test_addCart(self):
        cart_obj = CartPage(self.driver)
        child = self.driver.window_handles
        self.driver.switch_to.window(child[1])

        print(cart_obj.get_productName().text)
        print(cart_obj.get_productPrice().text)

        cart_obj.wait_explicit(CartPage.addingCart)
        cart_obj.adding_cart().click()

 #error in remove cart test case
    def test_removeCart(self):
        remove_obj = RemoveCart(self.driver)

        remove_obj.wait_explicit(remove_obj.removing)
        # removing from the cart
        remove_obj.remove_cart().click()

        remove_obj.wait_explicit(remove_obj.remove_confirmation())
        remove_obj.remove_confirmation().click()


    def test_logout(self):
        logout_obj = LogoutPage(self.driver)

        logout_obj.wait_explicit(logout_obj.logOption)
        logout_obj.log_option().click()

        logout_obj.wait_explicit(logout_obj.clickLogout)
        logout_obj.clicK_logout().click()

        #actions = ActionChains(self.driver)
        #actions.move_to_element(logg).move_to_element(logging).click().perform()

    @pytest.fixture(params=TestData.Login_data)
    def getData(self, request):
        return request.param

    @pytest.fixture(params=TestData.product_data)
    def searchproduct(self, request):
        return request.param


