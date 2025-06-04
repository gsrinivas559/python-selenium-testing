# Locators - are used to identify elements in the dom(Document Object Model)
# Locator types - ID, Xpath, CSSSelector, ClassName, Name, LinkText
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()  # chrome driver initiation
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")  # testing rahul shetty practice page
driver.implicitly_wait(10)

# Scenario - filling the form details and submitting the form. Check success alert message after submission
# finding elements using specific locators
# Xpath --> //tagName[@attributeName='Value']
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("test")
driver.find_element(By.NAME, "email").send_keys("test@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("test@123")

# CSS --> //tagName[@attributeName='Value'], for id - #idValue and for className - .className
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# Static Dropdowns
# Select --> if the element is having select tag, then we can use select class methods to perform actions
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(2)  # To visually view the output
dropdown.select_by_index(0)  # male will be selected and index starts from 0
time.sleep(2)  # To visually view the output
# dropdown.select_by_value()  # pass the value attribute value, commented due to value attribute not present in element

driver.find_element(By.CLASS_NAME, "btn-success").click()
alertMessage = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
print(alertMessage)  # Success! The Form has been submitted successfully!.

assert "Success" in alertMessage

driver.find_element(By.CSS_SELECTOR, "input[name='name']:nth-child(1)").send_keys("Automation")
time.sleep(2)  # To visually view the output
driver.find_element(By.CSS_SELECTOR, "input[name='name']:nth-child(1)").clear()
time.sleep(2)  # To visually view the output

driver.quit()
