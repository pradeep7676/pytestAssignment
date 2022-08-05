import logging
import time
import unittest

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
from selenium.webdriver.common.keys import Keys

class TestShopping(Base):


    def test_searchProduct(self, searchproduct, getData):
        self.driver.implicitly_wait(5)
        LoginPage.login_creditionals(self,credi=getData)
        sp_obj = SearchProduct(self.driver)

        sp_obj.wait_explicit(sp_obj.productType)
        time.sleep(1)

        sp_obj.product_type().send_keys(searchproduct['item'])
        sp_obj.product_type().send_keys(Keys.ENTER)

        # sp_obj.wait_explicit(sp_obj.search)
        # sp_obj.search_product().click()

        sp_obj.wait_explicit(sp_obj.produc)
        sp_obj.product().click()
        sp_val = self.driver.title
        if sp_val == "Iphone- Buy Products Online at Best Price in India - All Categories | Flipkart.com":
            assert True
        else:
            assert False

    def test_addCart(self):
        cart_obj = CartPage(self.driver)
        child = self.driver.window_handles
        self.driver.switch_to.window(child[1])

        print(cart_obj.get_productName().text)
        print(cart_obj.get_productPrice().text)

        cart_obj.wait_explicit(CartPage.addingCart)
        cart_obj.adding_cart().click()

        cart_val = self.driver.title
        assert "APPLE" in cart_val




    def test_removeCart(self):
        remove_obj = RemoveCart(self.driver)

        remove_obj.wait_explicit(remove_obj.removing)
        # removing from the cart
        remove_obj.remove_cart().click()

        remove_obj.wait_explicit(remove_obj.remove_confirmation())
        remove_obj.remove_confirmation().click()

        remove_val = self.driver.title
        assert "APPLE" in remove_val


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


