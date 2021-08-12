import pytest
from selenium import webdriver


def driver_factory(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'opera':
        driver = webdriver.Firefox()
    elif browser == 'safari':
        driver = webdriver.Firefox()
    else:
        raise Exception('Driver not supported')
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.3.13:8081")


@pytest.fixture
def browser(request):
    driver = driver_factory(request.config.getoption("--browser"))
    url = request.config.getoption("--url")
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    driver.url = url
    driver.admin_url = 'http://192.168.3.13:8888'

    return driver
