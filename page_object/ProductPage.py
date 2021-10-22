from .BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    BREADCRUMB = (By.CSS_SELECTOR, '.breadcrumb')
    ADD_TO_CARD = (By.ID, 'button-cart')
    CARD_TOTAL = (By.CSS_SELECTOR, '#cart > button')
    DESCRIPTION = (By.CSS_SELECTOR, '.tab-content')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.btn-default')
    ALERT = (By.CSS_SELECTOR, '.alert-success')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.open('/macbook')

    def verify_breadcrumb_element(self):
        return self._is_element_presence(self.BREADCRUMB)

    def get_breadcrumb_text(self):
        return self._get_element_text(self.BREADCRUMB)

    def verify_card_total_element(self):
        return self._is_element_presence(self.CARD_TOTAL)

    def get_alert_text(self):
        return self._get_element_text(self.ALERT)

    def click_button_card_element(self):
        btn = self._is_element_presence(self.ADD_TO_CARD)
        self._click_element(btn)

    def verify_description_element(self):
        return self._is_element_presence(self.DESCRIPTION)
