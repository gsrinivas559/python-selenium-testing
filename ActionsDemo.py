import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # chrome driver initiation
driver.implicitly_wait(5)  # globally wait applied
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/#/")  # testing rahul shetty practice page

# Scenario - Perform mouse over action on mouseover example
actions = ActionChains(driver)
# move_to_element --> performs moving to specific element
# .perform() --> to perform the action
# actions.double_click(driver.find_element(By.)) --> performs double click on element
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform()
time.sleep(2)  # To visually view the output
# context_click --> perform right click action
# actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
# time.sleep(2)  # To visually view the output
actions.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

time.sleep(2)  # To visually view the output
driver.quit()
