from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.get("https://demoqa.com/frames")

#Frames
driver.switch_to.frame("frame2")
data=driver.find_element(By.ID,"sampleHeading").text
print(data)
driver.switch_to.default_content()
print(driver.title)
time.sleep(3)

#Screenshot
# driver.save_screenshot("ss.png")
driver.get_screenshot_as_png()
