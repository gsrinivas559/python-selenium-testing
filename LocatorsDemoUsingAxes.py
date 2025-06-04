import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # chrome driver initiation
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client/")  # testing rahul shetty practice page
driver.implicitly_wait(10)

# Scenario - to click on forgot password and perform password reset
# to use LINK_TEXT, the element should contains tag name as a(anchor tag)
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
# Xpath and CSS Axes - traversing through parent and child
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.XPATH, "//label[text()='Confirm Password']/following-sibling::input").send_keys("Hello@1234")
# driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
driver.find_element(By.XPATH, "//form/div[4]/child::button[text()='Save New Password']").click()
time.sleep(2)  # To visually view the output

driver.quit()
