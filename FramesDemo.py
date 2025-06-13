from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # chrome driver initiation
driver.implicitly_wait(5)  # globally wait applied
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/nested_frames")  # testing automation practice page

#  Scenario - switching between nested frames
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-left")
print(driver.find_element(By.CSS_SELECTOR, "body").text)  # LEFT

driver.switch_to.default_content()

driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-middle")
print(driver.find_element(By.CSS_SELECTOR, "body").text)  # MIDDLE

driver.switch_to.default_content()

driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-right")
print(driver.find_element(By.CSS_SELECTOR, "body").text)  # RIGHT

driver.switch_to.default_content()

driver.switch_to.frame("frame-bottom")
print(driver.find_element(By.CSS_SELECTOR, "body").text)  # BOTTOM

driver.switch_to.default_content()

driver.quit()