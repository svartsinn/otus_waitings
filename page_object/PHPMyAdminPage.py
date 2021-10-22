from .BasePage import BasePage
from selenium.webdriver.common.by import By


class PHPMyAdminPage(BasePage):
    PANEL = (By.ID, 'navipanellinks')
    MENU = (By.CSS_SELECTOR, '.menucontainer')
    LANGUAGES = (By.ID, 'sel-lang')
    DROPLIST = (By.CSS_SELECTOR, '.drop_list')
    DOCUMENTS = (By.ID, 'maincontainer')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('http://localhost:8888')

    def verify_panel_element(self):
        return self._is_element_presence(self.PANEL)

    def verify_menu_element(self):
        return self._is_element_presence(self.MENU)

    def count_dropdown_list(self):
        return len(self._select_dropdown_list(self.LANGUAGES).options)

    def count_elements(self):
        return len(self._elements_by_selector(self.DROPLIST))

    def verify_doc_element(self):
        return self._is_element_presence(self.DOCUMENTS)
