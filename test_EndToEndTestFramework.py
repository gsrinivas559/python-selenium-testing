import json
import os.path

import pytest

from pageObjects.LoginPage import LoginPage
# pytest -m smoke // tagging
# pytest -n 10 // pytest-xdist plugin you need to run in parallel
# pytest -n 3 -m smoke --browserName edge  --html reports/report.html

# Scenario - login and select a product from product list, checkout and purchase the product in the shop
# test_data_path = os.path.dirname(os.path.realpath(__file__))
projectPath = os.getcwd()
jsonFilePath = projectPath + '/data/test_EndToEndTestFramework.json'
with open(jsonFilePath) as f:
    # converting json data to python object
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_EndToEnd(browserInstance, test_list_item):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")  # testing rahul shetty practice page
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    shopPage = loginPage.login(test_list_item["username"], test_list_item["password"])
    shopPage.add_product_to_cart(test_list_item["product"])
    print(shopPage.getTitle())
    checkoutConfirmationPage = shopPage.goToCart()
    checkoutConfirmationPage.checkout()
    checkoutConfirmationPage.enter_delivery_address(test_list_item["country"])
    checkoutConfirmationPage.validate_order()
