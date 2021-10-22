from ..BasePage import BasePage
from selenium.webdriver.common.by import By


class FooterElement(BasePage):
    FOOTER = (By.XPATH, "//*[contains(text(), 'My Account')]")

    def verify_footer_element(self):
        return self._is_element_presence(self.FOOTER)
