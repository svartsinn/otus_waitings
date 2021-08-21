from ..BasePage import BasePage
from selenium.webdriver.common.by import By


class SuccessAlert(BasePage):
    ALERT = (By.CSS_SELECTOR, ".alert-success")

    def get_text_from_alert(self):
        return self._get_element_text(self.ALERT)
