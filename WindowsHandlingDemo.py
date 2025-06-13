import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # chrome driver initiation
driver.implicitly_wait(5)  # globally wait applied
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")  # testing automation practice page

# Scenario - switch to child window, validate text, switch back to parent window and perform validation
driver.find_element(By.CSS_SELECTOR, "#content a").click()

# driver.window_handles --> retrieves the specific window handles id's opened in browser
windowHandlesList = driver.window_handles

# switching to child window. parent window stored in 0 index and child window stored in 1 index in list
driver.switch_to.window(windowHandlesList[1])

assert driver.find_element(By.TAG_NAME, "h3").text == "New Window"
driver.close()
time.sleep(2)  # To visually view the output

# switching back to parent window.
driver.switch_to.window(windowHandlesList[0])

assert driver.find_element(By.TAG_NAME, "h3").text == "Opening a new window"

time.sleep(2)  # To visually view the output
driver.quit()
