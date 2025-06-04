import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# browser can be initiated by importing right package
# Servcie class - used for creating instance for local driver and other way to create instance of driver
# service_obj = Service("./chromedriver") # Need to pass chrome driver path
# driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome() # chrome driver initiation
# driver = webdriver.Firefox()  # firefox driver initiation
# driver = webdriver.Edge()   # edge driver initiation
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.google.com")

time.sleep(2)  # to visually see the driver initiation, we are keeping 2 seconds wait
driver.quit()  # to quit the driver instance