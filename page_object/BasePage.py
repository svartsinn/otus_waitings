import logging

import allure

from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, wait=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)
        self.logger = logging.getLogger(type(self).__name__)

    @allure.step("Verify element {locator} on page")
    def _is_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, self.driver.t).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                name=self.driver.session_id,
                body=self.driver.get_screenshot_as_png,
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f'Element with locator {locator} not found on the page')

    def _element(self, locator: tuple):
        self.logger.info(f"Check element with locator {locator} precense")
        return self._is_element_presence(locator)

    def _elements_by_selector(self, locator: tuple):
        self.logger.info(f"Find element with locator {locator}")
        return self.driver.find_elements(*locator)

    @allure.step("Verify element {locator} text")
    def _get_element_text(self, locator: tuple):
        self.logger.info(f"Get element {locator} text")
        return self._is_element_presence(locator).text

    def _click_element(self, element):
        self.logger.info(f"Click element {element}")
        ActionChains(self.driver).pause(0.3).move_to_element(element).click().perform()

    def _simple_click_element(self, element):
        self.logger.info("Element {} click".format(element))
        element.click()

    @allure.step("Send text {text} to element {element}")
    def _send_keys_to_element(self, element, text: str):
        self.logger.info(f"Send keys {text} to element {element}")
        return element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def _select_dropdown_list(self, locator: tuple):
        self.logger.info(f"Select dropdown list for {locator}")
        return Select(self._is_element_presence(locator))

    @allure.step("Mark checkbox {locator}")
    def _mark_checkbox(self, locator: tuple):
        self.logger.info(f"Mark checkbox {locator}")
        el = self._is_element_presence(locator)
        self._click_element(el)

    def _fill_input(self, locator: tuple, text: str):
        el = self._is_element_presence(locator)
        self._send_keys_to_element(el, text)

    @allure.step("Click on element {locator}")
    def _click(self, locator: tuple):
        element = self._element(locator)
        ActionChains(self.driver).pause(0.3).move_to_element(element).click().perform()

    def accept_alert(self):
        self.logger.info("Accept alert window")
        WebDriverWait(self.driver, self.driver.t).until(EC.alert_is_present())
        alert = self.driver.switch_to_alert()
        alert.accept()
