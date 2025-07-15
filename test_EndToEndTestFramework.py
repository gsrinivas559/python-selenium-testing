import json
import os.path

import pytest

from pageObjects.LoginPage import LoginPage

# Scenario - login and select a product from product list, checkout and purchase the product in the shop
# test_data_path = os.path.dirname(os.path.realpath(__file__))
projectPath = os.getcwd()
jsonFilePath = projectPath + "\\data\\test_EndToEndTestFramework.json"
with open(jsonFilePath) as f:
    # converting json data to python object
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.parametrize("test_list_item", test_list)
def test_EndToEnd(browserInstance, test_list_item):
    driver = browserInstance
    loginPage = LoginPage(driver)
    shopPage = loginPage.login(test_list_item["username"], test_list_item["password"])
    shopPage.add_product_to_cart(test_list_item["product"])
    checkoutConfirmationPage = shopPage.goToCart()
    checkoutConfirmationPage.checkout()
    checkoutConfirmationPage.enter_delivery_address(test_list_item["country"])
    checkoutConfirmationPage.validate_order()
