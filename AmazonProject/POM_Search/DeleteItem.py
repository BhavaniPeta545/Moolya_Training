import time

from selenium.webdriver.common.by import By

from utilities.BasePage import  BasePage


class DeleteItem(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def __int__(self,driver):
        self.driver=driver

    delete_icon=(By.XPATH,"//input[@title='Delete']")
    cart_data=(By.XPATH,"//div[@id='nav-cart-count-container']//span[@id='nav-cart-count']")


    def delete_item(self):
        self.driver.implicitly_wait(10)
        self.do_click(self.delete_icon)
        time.sleep(10)

    def verify_delete(self):
        success_message=self.get_text(self.cart_data)
        print(success_message)
        assert success_message=="0"
