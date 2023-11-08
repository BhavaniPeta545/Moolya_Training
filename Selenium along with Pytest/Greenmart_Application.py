from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR,"input[type='search']").send_keys("ca")
time.sleep(5)

#list of elements with search "ca"
veglist=driver.find_elements(By.XPATH,"(//div[@class='products'])//div[@class='product']")
print("The length of the vegetable list is ",len(veglist))
# for i in veglist:
#     print(i.text)

#AddItems to Cart
items=driver.find_elements(By.XPATH,"//div[@class='product-action']//button[text()='ADD TO CART']")
for i in items:
    i.click()

time.sleep(5)
driver.find_element(By.XPATH,"//a[@class='cart-icon']//img").click()
driver.find_element(By.XPATH,"(//div[@class='action-block']//button)[1]").click()

#Adding the items price
rows=driver.find_elements(By.XPATH,"//table[@class='cartTable']//tbody//tr")
print(len(rows))
cols=driver.find_elements(By.XPATH,"//table[@class='cartTable']//tbody//tr[1]//td")
print(len(cols))
lastcol=len(cols)
total_cost=0
for r in range(1,len(rows)+1):
    total_cost+=int(driver.find_element(By.XPATH,"//table[@class='cartTable']//tbody//tr["+str(r)+"]//td["+str(lastcol)+"]").text)
print(total_cost)
time.sleep(10)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
total_amount=int(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print(total_amount)
time.sleep(10)
assert total_amount == total_cost
time.sleep(5)

#Placing Order
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
time.sleep(10)
country=Select(driver.find_element(By.XPATH,"//select"))
count=country.options
for value in count:
    if value.text=="India":
        value.click()
driver.find_element(By.CSS_SELECTOR,".chkAgree").click()
driver.find_element(By.XPATH,"//button[text()='Proceed']").click()
time.sleep(3)
# driver.execute_script("window.stop()")
success_prompt=driver.find_element(By.XPATH,"(//div[@class='products']//span)[1]").text
assert success_prompt=="""Thank you, your order has been placed successfully
You'll be redirected to Home page shortly!!"""

