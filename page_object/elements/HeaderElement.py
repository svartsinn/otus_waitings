from ..BasePage import BasePage
from selenium.webdriver.common.by import By


class HeaderElement(BasePage):
    PARENT = (By.ID, 'top')
    CURRENCY_LIST = (By.CSS_SELECTOR, '#form-currency > div > button > span')
    POUND = (By.NAME, 'GBP')

    def click_on_currency_list(self):
        el = self._is_element_presence(self.CURRENCY_LIST)
        self._click_element(el)

    def click_on_pound(self):
        el = self._is_element_presence(self.POUND)
        self._click_element(el)
