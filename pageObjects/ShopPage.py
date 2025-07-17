from selenium.webdriver.common.by import By

from pageObjects.Checkout_ConfirmationPage import CheckoutConfirmationPage
from utils.BrowserUtils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shopLink = (By.CSS_SELECTOR, "a[href*='shop']")
        self.products = (By.CSS_SELECTOR, "div.card")
        self.productName = (By.CSS_SELECTOR, ".card-title a")
        self.addToCart = (By.CSS_SELECTOR, ".card-footer button")
        self.checkoutButton = (By.CSS_SELECTOR, "a.btn-primary")

    def add_product_to_cart(self, productToSelect):
        self.driver.find_element(*self.shopLink).click()
        productElements = self.driver.find_elements(*self.products)
        for productElement in productElements:
            productTitle = productElement.find_element(*self.productName).text
            if productTitle == productToSelect:
                productElement.find_element(*self.addToCart).click()

    def goToCart(self):
        self.driver.find_element(*self.checkoutButton).click()
        checkoutConfirmationPage = CheckoutConfirmationPage(self.driver)
        return checkoutConfirmationPage
