from selenium.webdriver.common.by import By


class GreenKartPage:

    def __init__(self, driver):
        self.driver = driver
        self.columnHeader = (By.XPATH, "//span[text()='Veg/fruit name']")
        self.vegFruitNames = (By.CSS_SELECTOR, "tr td:nth-child(1)")

    # clicking on column header
    def clickColumnHeader(self):
        self.driver.find_element(*self.columnHeader).click()

    def validateVeggiesSorted(self):
        # collecting all listed veg/fruits name
        collectedList = []
        vegFruitsElements = self.driver.find_elements(*self.vegFruitNames)
        for element in vegFruitsElements:
            collectedList.append(element.text)

        # copying the collected list into another list before sorting
        originalList = collectedList.copy()

        # Applying sorting
        collectedList.sort()

        # Validating the both lists
        assert originalList == collectedList
