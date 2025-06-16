import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # chrome driver initiation
driver.implicitly_wait(5)  # globally wait applied
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")  # testing rahul shetty practice page

# Scenario - sort the veg/fruit name table and validate the sorting performed
# clicking on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

collectedList = []
# collecting all listed veg/fruits name
vegFruitsElements = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(1)")
for element in vegFruitsElements:
    collectedList.append(element.text)

# copying the collected list into another list before sorting
originalList = collectedList.copy()

# Applying sorting
collectedList.sort()

# Validating the both lists
assert originalList == collectedList

time.sleep(2)  # To visually view the output
driver.quit()
