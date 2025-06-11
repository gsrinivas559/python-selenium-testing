import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()  # chrome driver initiation
driver.implicitly_wait(5)  # globally wait applied
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")  # testing rahul shetty practice page

# End to End Testcase to Automate ecommerce GreenKart Application
# Scenario - search partial name of vegetable and add to cart all the items matching
# proceed to checkout, apply promo code and validate the items discounts
driver.find_element(By.CSS_SELECTOR, ".search-form input[class='search-keyword']").send_keys("ber")
time.sleep(2)
productResults = driver.find_elements(By.CSS_SELECTOR, ".products div.product")
print(len(productResults))
assert len(productResults) > 0
for productResult in productResults:
    productResult.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()

driver.find_element(By.CSS_SELECTOR, "a.cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, "input.promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)  # Explict wait applied to specific element
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
promoMessage = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(promoMessage)
assert promoMessage == "Code applied ..!"
