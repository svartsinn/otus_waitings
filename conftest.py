import logging

from faker import Faker
import os
import pytest
from selenium import webdriver

filename = 'logs/selenium.log'
os.makedirs(os.path.dirname(filename), exist_ok=True)
file_handler = logging.FileHandler(filename, mode="w", encoding=None, delay=False)
logging.basicConfig(level=logging.INFO, filename=filename, force=True)


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--bversion", default="92.0")
    parser.addoption("--executor", action="store", default="localhost")
    parser.addoption("--url", action="store", default="https://demo.opencart.com")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--tolerance", type=int, default=3)


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    url = request.config.getoption("--url")
    tolerance = request.config.getoption("--tolerance")
    logger = logging.getLogger("BrowserLogger")
    test_name = request.node.name

    if executor == "localhost":
        caps = {'goog:chromeOptions': {}}
        wd = webdriver.Chrome(desired_capabilities=caps)
    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            'browserName': browser,
            'browserVersion': version,
            'screenResolution': '1280x1024',
            'name': 'arg tests',
            'selenoid:options': {
                'sessionTimeout': '60s',
                'enableVNC': vnc,
                'enableVideo': videos,
                'enableLog': logs,
            },
        }
        wd = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )

    logger.info("===> Test {} started".format(test_name))

    def open(path=''):
        return wd.get(url + path)

    wd.maximize_window()
    wd.open = open
    # wd.open()
    wd.t = tolerance

    def fin():
        wd.quit()
        logger.info("===> Test {} finished".format(test_name))

    request.addfinalizer(fin)
    return wd


@pytest.fixture(scope="function")
def new_user():
    fake = Faker()
    result = {'first_name': fake.first_name(),
              'last_name': fake.last_name(),
              'email': fake.email(),
              'phone': fake.phone_number(),
              'password': fake.password(length=12)}
    return result
