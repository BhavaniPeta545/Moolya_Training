from selenium.webdriver.common.by import By

from utilities.BasePage import  BasePage


class AddtoCart(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def __int__(self,driver):
        self.driver=driver

    addtocart=(By.XPATH,"//div[@class='a-button-stack']")
    added_message=(By.ID,"NATC_SMART_WAGON_CONF_MSG_SUCCESS")


    def add_to_cart(self):
        self.driver.implicitly_wait(10)
        self.scroll_till_element(self.addtocart)
        self.do_click(self.addtocart)

    def verify_cart(self):
        success_message=self.get_text(self.added_message)
        print(success_message)
        assert success_message=="Added to Cart"
