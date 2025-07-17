from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.BrowserUtils import BrowserUtils


class CheckoutConfirmationPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, "button.btn-success")
        self.country_input = (By.CSS_SELECTOR, "#country")
        self.checkbox = (By.CSS_SELECTOR, "div.checkbox label")
        self.purchase_button = (By.CSS_SELECTOR, "input[value='Purchase']")
        self.alert_message = (By.CSS_SELECTOR, "div.alert")

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self, countryToSelect):
        self.driver.find_element(*self.country_input).send_keys(countryToSelect)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, countryToSelect)))
        self.driver.find_element(By.LINK_TEXT, countryToSelect).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.purchase_button).click()

    def validate_order(self):
        alertMessage = self.driver.find_element(*self.alert_message).text
        assert "Success!" in alertMessage
