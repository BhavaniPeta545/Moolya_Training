import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from POM_Search.ADDtoCart import AddtoCart
from POM_Search.DeleteItem import DeleteItem
from POM_Search.Filter_By_Price_Page import FilterByPrice
# from testcases.BaseTest import BaseTest
from POM_Search.Search_Page import Search
# from testcases.conftest import BaseTest

@pytest.mark.usefixtures("setup")
class Test_Search():
    #
    # def __init__(self,driver):
    #     self.driver=driver


    # def test_login1(self,setup):
    #     objlogin = Login(setup)
    #     objlogin.login("Admin","admin123")
    #     time.sleep(10)

    # def test_search(self,setup):
    #     objSearch= Search(setup)
    #     objSearch.search_shirts()
    #     time.sleep(10)

    # handles=[]


    def test_select_item_with_filters(self, setup):
        objFilter=FilterByPrice(setup)
        objFilter.filter_by_price_and_select_item()

    def test_add_to_cart(self, setup):
        obj1 = AddtoCart(setup)
        obj1.add_to_cart()
        obj1.verify_cart()

    def test_delete_item_in_cart(self,setup):
        objdelete=DeleteItem(setup)
        objdelete.delete_item()
        objdelete.verify_delete()




    # def test_add_to_cart(self,setup):
    #     objCart=AddtoCart(setup)
    #     objFilter = FilterByPrice(setup)
    #     FilterByPrice.filter_by_price_and_select_item()
    #     objCart.add_to_cart()







