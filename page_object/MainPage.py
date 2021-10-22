from .BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    IMAGE = (By.CSS_SELECTOR, '.image')
    TITLE = (By.CSS_SELECTOR, '#content > h3')
    BASKET = (By.ID, 'cart-total')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.open('/')

    def count_image_on_page(self):
        return len(self._elements_by_selector(self.IMAGE))

    def get_title_text(self):
        return self._get_element_text(self.TITLE)

