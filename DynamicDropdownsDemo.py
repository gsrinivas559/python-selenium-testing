import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # chrome driver initiation
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")  # testing rahul shetty practice page
driver.implicitly_wait(10)

# Scenario - select country auto suggestion dropdown
countryDropdown = driver.find_element(By.CSS_SELECTOR, "#autosuggest")
countryDropdown.click()
countryDropdown.send_keys("Ind")
time.sleep(2)  # dropdown options to appear
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

selectedCountry = countryDropdown.get_attribute("value")
print(selectedCountry + " == India")
assert selectedCountry == "India"
