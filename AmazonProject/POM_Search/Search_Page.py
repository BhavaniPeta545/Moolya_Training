import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.BasePage import  BasePage


class Search(BasePage):
    search=(By.ID,"twotabsearchtextbox")#id with css
    search_icon=(By.ID,"nav-search-submit-button")#id
    search_list=(By.XPATH,"//div[@class='two-pane-results-container']")#xpath

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver
        # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def get_title(self, title):
        return self.get_title(title)

    # def login(self, username, password):
    #     self.do_send_keys(self.username, username)
    #     self.do_send_keys(self.password, password)
    #     self.do_click(self.login_submit_btn)

    def search_shirts(self):
        self.do_send_keys(self.search,"shirts")
        time.sleep(5)
        print(self.get_list(self.search_list))
        self.do_click(self.search_icon)


