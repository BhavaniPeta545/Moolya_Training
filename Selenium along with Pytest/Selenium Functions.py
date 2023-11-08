import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#Creating a service object
service_obj=Service()
driver=webdriver.Chrome(service=service_obj)

#Navigating to a page and getting title of the page
driver.get("https://www.amazon.in/GRECIILOOKS-Geometric-Regular-Shirt-GL-MS-6064_Multicolour/dp/B0BZV4RF4Y/ref=sr_1_3_sspa?crid=1GGGN7K60T3Q6&keywords=shirts&qid=1699106739&sprefix=shirts+%2Caps%2C236&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)


#Dropdown Example
drp=Select(driver.find_element(By.ID,"dropdown-class-example"))
drp.select_by_visible_text("Option3")
time.sleep(5)
drp.select_by_index(1)
time.sleep(5)
res=drp.options
print(len(res))
for i in res:
    print(i.text)

#Autocomplete
driver.find_element(By.ID,"autocomplete").send_keys("in")
time.sleep(3)
li=driver.find_elements(By.CLASS_NAME,"ui-menu-item")
for j in li:
    if j.text=="India":
        j.click()
c=driver.find_element(By.ID,"autocomplete").is_enabled()
ele=j.is_displayed()
print(ele)
time.sleep(9)

#Checkbox Example
check=driver.find_elements(By.XPATH,"//label//input[@type='checkbox']")
print(len(check))
for ck in check:
    if ck.get_attribute("value")=="option3":
        ck.click()
        print(ck.is_enabled())
        time.sleep(3)

#Alerts
driver.find_element(By.ID,"name").send_keys("bhavani")
time.sleep(5)
driver.find_element(By.ID,"confirmbtn").click()
a=driver.switch_to.alert
time.sleep(5)
textmsg=a.text
assert textmsg=="Hello bhavani, Are you sure you want to confirm?","messge error"
# a.accept()
time.sleep(5)

#Show/Hide Textbox
driver.find_element(By.ID,"show-textbox").click()
driver.find_element(By.ID,"hide-textbox").click()
time.sleep(5)
print(driver.find_element(By.ID,"displayed-text").is_displayed())

#Switch to Window
driver.find_element(By.LINK_TEXT,"Open Tab").click()
driver.switch_to.window()
# element=driver.find_element(By.LINK_TEXT,"Access all our Courses")
wait=WebDriverWait(driver,30)
wait.until(EC.presence_of_element_located(By.LINK_TEXT,"Access all our Courses"))

#Scroll function with JavaScriptExecutor

driver.execute_script("window.scrollBy(0,10000)","")
Element=driver.find_element(By.XPATH,"(//div[@class='left-align'])[4]")
driver.execute_script("arguments[0].scrollIntoView();",Element)


#ActionChains
action=ActionChains(driver)
action.move_to_element((driver.find_element(By.ID,"mousehover"))).perform()
time.sleep(10)
# action.key_down(Keys.ARROW_DOWN).perform()
action.double_click(By.LINK_TEXT,("Top")).click().perform()
action.key_down(Keys.CONTROL,"a").key_up(Keys.CONTROL).perform()



