import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()  # chrome driver initiation
driver.implicitly_wait(5)  # globally wait applied
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/#/")  # testing rahul shetty practice page
wait = WebDriverWait(driver, 10)

# Scenario - perform window switching, fetch the emailId from text and signin the form
driver.find_element(By.CSS_SELECTOR, ".float-right a.blinkingText:nth-child(1)").click()

windowsList = driver.window_handles
driver.switch_to.window(windowsList[1])

wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "p.red")))
textValue = driver.find_element(By.CSS_SELECTOR, "p.red").text
print(textValue)  # Please email us at mentor@rahulshettyacademy.com with below template to receive response
# Method 1 --> using slicing
print(textValue[19:48])  # mentor@rahulshettyacademy.com
emailID = textValue[19:48]

# Method 2 --> using split and strip
print(textValue.split("at")[1])  # mentor@rahulshettyacademy.com with below templ
print(textValue.split("at")[1].strip())  # mentor@rahulshettyacademy.com with below templ
print(textValue.split("at")[1].strip().split(" ")[0])  # mentor@rahulshettyacademy.com

driver.close()
driver.switch_to.window(windowsList[0])

driver.find_element(By.ID, "username").send_keys(emailID)
driver.find_element(By.NAME, "password").send_keys("learning")
driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()

wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div.alert")))
print(driver.find_element(By.CSS_SELECTOR, "div.alert").text)

assert driver.find_element(By.CSS_SELECTOR, "div.alert").text == "Incorrect username/password."

time.sleep(2)  # To visually view the output
driver.quit()
