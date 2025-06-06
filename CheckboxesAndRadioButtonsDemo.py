import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # chrome driver initiation
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")  # testing rahul shetty practice page
driver.implicitly_wait(10)

# Scenario - check 'option 2' checkbox from the checkbox example assuming options dynamically changes
checkBoxes = driver.find_elements(By.CSS_SELECTOR, "div[id='checkbox-example'] input[type='checkbox']")
print(len(checkBoxes))

for checkBox in checkBoxes:
    if checkBox.get_attribute("value") == "option2":
        checkBox.click()
        assert checkBox.is_selected()
        break

# Scenario - select 'radio 3' radio button from the radio button example assuming options dynamically changes
radioButtons = driver.find_elements(By.CSS_SELECTOR, "div[id='radio-btn-example'] input[type='radio']")
print(len(radioButtons))

# if the options are static and cannot change positions
# radioButtons[2].click()
# assert radioButtons[2].is_selected()

for radioButton in radioButtons:
    if radioButton.get_attribute("value") == "radio3":
        radioButton.click()
        assert radioButton.is_selected()
        break

# Scenario - Checking element is displayed in element displayed example
assert driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed()
# we hide the element and then verify
driver.find_element(By.XPATH, "//input[@id='hide-textbox']").click()
# Returns exception when element is checked, so using not condition to ignore the exception
assert not driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed()

time.sleep(2)  # To visually view the output
driver.quit()
