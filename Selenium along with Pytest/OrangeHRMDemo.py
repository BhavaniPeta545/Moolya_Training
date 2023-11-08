import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#
service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
# driver=webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
# driver=webdriver.Firefox(service=service_obj)
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

#Login
driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(5)

#Navigating to a module called PIM
driver.find_element(By.LINK_TEXT,"PIM").click()
time.sleep(10)

#Dropdown with Select class
res=Select(driver.find_element(By.XPATH,"(//div[@class='oxd-select-wrapper'])[1]"))
res.select_by_visible_text("Freelance")
time.sleep(10)

#Entering data in Textbox
res=driver.find_element(By.XPATH,"(//input[@placeholder='Type for hints...'])[1]")
res.click()
res.send_keys("ch")
time.sleep(7)

#Autocomplete Action
name = driver.find_elements(By.XPATH,"(//div[@class='oxd-autocomplete-dropdown --positon-bottom']//div[@role='option'])")
print(len(name))
driver.find_element(By.XPATH,"(//div[@class='oxd-autocomplete-dropdown --positon-bottom']//div[@role='option'])[1]").click()
time.sleep(5)

#Scrolling into Element
driver.execute_script("window.scrollTo(0,2000)")
link=driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc")
driver.execute_script("arguments[0].scrollIntoView();",link)
time.sleep(6)

#Window HAndling
driver.find_element(By.ID,"openwindow").click()
time.sleep(5)
handle=driver.window_handles
driver.switch_to.window(handle[1])#child
print(driver.title)
driver.close()
driver.switch_to.window(handle[0])# parent
print(driver.title)
time.sleep(5)

#Logout
driver.find_element(By.CSS_SELECTOR,".oxd-userdropdown-name").click()
time.sleep(4)
driver.find_element(By.LINK_TEXT,"Logout").click()











