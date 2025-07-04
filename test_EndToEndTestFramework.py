from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_EndToEnd(browserInstance):
    driver = browserInstance
    driver.implicitly_wait(5)  # globally wait applied
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")  # testing rahul shetty practice page
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("rahulshettyacademy")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("learning")
    driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
    # Scenario - select a product from product list, checkout and purchase the product in the shop
    driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
    productToSelect = "Nokia Edge"
    productElements = driver.find_elements(By.CSS_SELECTOR, "div.card")
    for productElement in productElements:
        productTitle = productElement.find_element(By.CSS_SELECTOR, ".card-title a").text
        if productTitle == productToSelect:
            productElement.find_element(By.CSS_SELECTOR, ".card-footer button").click()

    driver.find_element(By.CSS_SELECTOR, "a.btn-primary").click()
    sleep(2)  # To visually view the output
    driver.find_element(By.CSS_SELECTOR, "button.btn-success").click()
    countryToSelect = "India"
    driver.find_element(By.CSS_SELECTOR, "#country").send_keys(countryToSelect)
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, countryToSelect)))
    driver.find_element(By.LINK_TEXT, countryToSelect).click()
    driver.find_element(By.CSS_SELECTOR, "div.checkbox label").click()
    driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()
    alertMessage = driver.find_element(By.CSS_SELECTOR, "div.alert").text
    assert "Success!" in alertMessage
