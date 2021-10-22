from .BasePage import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    FIRST_NAME = (By.ID, 'input-firstname')
    LAST_NAME = (By.ID, 'input-lastname')
    EMAIL = (By.ID, 'input-email')
    PHONE = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, 'input-password')
    PASSWORD_CONFIRM = (By.ID, 'input-confirm')
    AGREE_CHECKBOX = (By.NAME, 'agree')
    SUBMIT = (By.CSS_SELECTOR, '.btn-primary')
    SUCCESS_TEXT = (By.CSS_SELECTOR, '#content > h1')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.open('/index.php?route=account/register')

    def fill_form(self, first_name, last_name, email, phone, password):
        self._fill_input(self.FIRST_NAME, first_name)
        self._fill_input(self.LAST_NAME, last_name)
        self._fill_input(self.EMAIL, email)
        self._fill_input(self.PHONE, phone)
        self._fill_input(self.PASSWORD, password)
        self._fill_input(self.PASSWORD_CONFIRM, password)
        self._mark_checkbox(self.AGREE_CHECKBOX)
        btn = self._is_element_presence(self.SUBMIT)
        self._click_element(btn)

    def get_success_text(self):
        return self._get_element_text(self.SUCCESS_TEXT)
