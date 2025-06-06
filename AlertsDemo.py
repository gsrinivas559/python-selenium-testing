import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # chrome driver initiation
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")  # testing rahul shetty practice page
driver.implicitly_wait(10)
# To handle java or javascript or browser alerts
# Scenario - enter text then click on alert then switch to alert and validate alert message contains text entered
name = "Srinivas"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
time.sleep(2)  # To visually view the alert appeared
alert = driver.switch_to.alert  # Switched to alert
print(alert.text)  # Hello Srinivas, share this practice page and share your knowledge
assert name in alert.text
alert.accept()  # To accept alert
# alert.dismiss() # To dismiss alert

driver.quit()
