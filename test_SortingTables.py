import pytest

from pageObjects.GreenKartPage import GreenKartPage


@pytest.mark.regression
def test_sortTables(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")  # testing rahul shetty practice page

    # Scenario - sort the veg/fruit name table and validate the sorting performed
    greenKartPage = GreenKartPage(driver)
    greenKartPage.clickColumnHeader()
    greenKartPage.validateVeggiesSorted()
