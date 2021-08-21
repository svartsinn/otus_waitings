from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def _is_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, self.browser.t).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError('Element with locator {} not found on the page'.format(locator))

    def _element(self, locator: tuple):
        return self._is_element_presence(locator)

    def _elements_by_selector(self, locator: tuple):
        return self.browser.find_elements(*locator)

    def _get_element_text(self, locator: tuple):
        return self._is_element_presence(locator).text

    def _click_element(self, element):
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _simple_click_element(self, element):
        element.click()

    def _send_keys_to_element(self, element, text: str):
        return element.send_keys(text)

    def get_current_url(self):
        return self.browser.current_url

    def _select_dropdown_list(self, locator: tuple):
        return Select(self._is_element_presence(locator))

    def _mark_checkbox(self, locator: tuple):
        el = self._is_element_presence(locator)
        self._click_element(el)

    def _fill_input(self, locator: tuple, text: str):
        el = self._is_element_presence(locator)
        self._send_keys_to_element(el, text)

    def _click(self, locator: tuple):
        element = self._element(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def accept_alert(self):
        WebDriverWait(self.browser, self.browser.t).until(EC.alert_is_present())
        alert = self.browser.switch_to_alert()
        alert.accept()
