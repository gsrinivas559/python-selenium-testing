import os

import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption("--browserName", action="store", default="chrome", help="Browser Selection")


@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browserName = request.config.getoption("browserName")
    if browserName == "chrome":
        driver = webdriver.Chrome()  # chrome driver initiation
    elif browserName == "edge":
        driver = webdriver.Edge()  # edge driver initiation

    driver.implicitly_wait(5)  # globally wait applied
    driver.maximize_window()
    yield driver  # before test function execution
    driver.quit()  # post test function execution


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            print("file_name: "+file_name)
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
