from faker import Faker
import pytest
from selenium import webdriver


def driver_factory(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'opera':
        driver = webdriver.Opera()
    elif browser == 'safari':
        driver = webdriver.Safari()
    else:
        raise Exception('Driver not supported')
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.3.13:8081")
    parser.addoption("--tolerance", type=int, default=3)



@pytest.fixture
def browser(request):
    driver = driver_factory(request.config.getoption("--browser"))
    url = request.config.getoption("--url")
    tolerance = request.config.getoption("--tolerance")

    driver.maximize_window()
    request.addfinalizer(driver.quit)
    driver.t = tolerance

    def open_url(path=''):
        return driver.get(url + path)

    driver.open = open_url
    driver.open()

    return driver


@pytest.fixture(scope="function")
def new_user():
    fake = Faker()
    result = {'first_name': fake.first_name(),
              'last_name': fake.last_name(),
              'email': fake.email(),
              'phone': fake.phone_number(),
              'password': fake.password(length=12)}
    return result
