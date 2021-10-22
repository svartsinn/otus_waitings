from .BasePage import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    TITLE = (By.CSS_SELECTOR, '#content > h2')
    DROPDOWN = (By.ID, 'input-sort')
    PAGE_NUM = (By.ID, 'input-limit')
    CAPTION = (By.CSS_SELECTOR, '.caption')
    COMPARE = (By.ID, 'compare-total')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.open('/smartphone')

    def get_title_text(self):
        return self._get_element_text(self.TITLE)

    def count_dropdown_list(self):
        return len(self._select_dropdown_list(self.DROPDOWN).options)

    def count_page_numbers(self):
        return len(self._select_dropdown_list(self.PAGE_NUM).options)

    def get_caption_text(self):
        return self._get_element_text(self.CAPTION)

    def get_compare_text(self):
        return self._get_element_text(self.COMPARE)
