import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class BasePage:

    def __init__(self, driver):
        self.driver = driver
    def do_click(self,locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_send_keys(self, locator, text):
        WebDriverWait(self.driver,  10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_title(self, title):
        WebDriverWait(self.driver,  10).until(EC.title_is(title))
        return self.driver.title

    def get_url(self,url):
        WebDriverWait(self.driver,10).until(EC.url_to_be(url))
        return self.driver.current_url

    def get_list(self,locator):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locator))
        list_res= [item.text for item in self.driver.find_elements(*locator)]
        return list_res

    def scroll_till_element(self,locator):

        # s=self.driver.find_element(*locator)
        # self.driver.execute_script(("arguments[0].scrollIntoView(true);",s))
        s = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(s))
        self.driver.execute_script("arguments[0].scrollIntoView();",s)

    # def open_page(self,url):
    #     return self.driver.get(url)

    def get_text(self,locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text
    def element_enebled(self,locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(*locator))
        return self.driver.find_element(*locator).is_enabled()

