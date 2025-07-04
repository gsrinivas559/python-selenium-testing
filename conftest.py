import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browserName", action="store", default="chrome", help="Browser Selection")


@pytest.fixture(scope="function")
def browserInstance(request):
    browserName = request.config.getoption("browserName")
    if browserName == "chrome":
        driver = webdriver.Chrome()  # chrome driver initiation
    elif browserName == "edge":
        driver = webdriver.Edge()  # chrome driver initiation
    yield driver  # before test function execution
    driver.close()  # post test function execution
