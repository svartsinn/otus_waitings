from ..BasePage import BasePage
from selenium.webdriver.common.by import By


class SearchElement(BasePage):
    SEARCH_INPUT = (By.NAME, 'search')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.btn-default')
    SEARCH_RESULT = (By.CSS_SELECTOR, '#content > h1')

    def submit_query_to_search(self, text):
        self._send_keys_to_element(self._element(self.SEARCH_INPUT), text)
        self._click(self.SEARCH_BUTTON)

    def verify_search_result(self):
        return self._is_element_presence(self.SEARCH_RESULT)

    def get_search_result_text(self):
        return self._get_element_text(self.SEARCH_RESULT)

    def click_on_search_button(self):
        self._click(self.SEARCH_BUTTON)
