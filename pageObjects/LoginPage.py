from selenium.webdriver.common.by import By

from pageObjects.ShopPage import ShopPage
from utils.BrowserUtils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username = (By.CSS_SELECTOR, "#username")
        self.password = (By.CSS_SELECTOR, "#password")
        self.signIn = (By.CSS_SELECTOR, "#signInBtn")

    # we can unpack tuple using * to split the tuple and send as parameters
    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signIn).click()
        shopPage = ShopPage(self.driver)
        return shopPage
