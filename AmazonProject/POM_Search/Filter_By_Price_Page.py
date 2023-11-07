import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from POM_Search.Search_Page import Search
from utilities.BasePage import  BasePage

class FilterByPrice(Search,BasePage):

    price_element=(By.CSS_SELECTOR,"#p_36-title")
    # range=(By.XPATH,"(//ul[@data-csa-c-slot-id='nav-ref'])[5]//span[@class='a-list-item']")
    low_range=(By.ID,"low-price")
    high_range=(By.ID,"high-price")
    search_range=(By.XPATH,"//input[@class='a-button-input']")

    # brand_element=(By.CSS_SELECTOR,"#p_89-title")
    # brand_name=(By.XPATH,"//ul[@data-csa-c-content-id='3837712031']//li[1]")


    def __init__(self,driver):
        super().__init__(self)
        self.driver=driver


    item = (By.XPATH,"//div[@data-asin='B087S6Q1M2']")

    def select_item(self):
        self.do_click(self.item)  # need to select from range of values

    def filter_by_price_and_select_item(self):
        self.search_shirts()
        self.scroll_till_element(self.price_element)
        self.do_send_keys(self.low_range,"200")
        self.do_send_keys(self.high_range,"500")
        self.do_click(self.search_range)
        time.sleep(5)
        self.scroll_till_element(self.item)
        self.select_item()
        time.sleep(10)
        # print(self.driver.title)
        # handles=self.driver.window_handles
        # self.driver.switch_to.window(handles[1])
        # print("----",self.driver.title)
        # return handles
        # assert self.driver.title=="Buy GRECIILOOKS Men's Geometric Regular Fit Shirt (GL-MS-6064_Black M) at Amazon.in"
        # print("shirt opened")

    # def filter_by_brand(self):
    #     self.search_shirts()
    #     # self.scroll_till_element(self.brand_element)
    #     self.do_click(self.brand_name)
    #     print(self.element_enebled(self.brand_name))
    #     time.sleep(10)






