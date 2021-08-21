from .BasePage import BasePage
from selenium.webdriver.common.by import By
import random


class AdminPage(BasePage):
    LOGIN = (By.ID, 'input-username')
    PASSWORD = (By.ID, 'input-password')
    SUBMIT = (By.CSS_SELECTOR, '.btn-primary')
    CATALOG = (By.ID, 'menu-catalog')
    PRODUCTS = (By.XPATH, "//*[contains(text(), 'Products')]")
    ADD_PRODUCT = (By.CSS_SELECTOR, '.fa-plus')
    DELETE_PRODUCT = (By.CSS_SELECTOR, '.btn-danger')
    PRODUCT_NAME = (By.ID, 'input-name1')
    TAG_TITLE = (By.ID, 'input-meta-title1')
    PRODUCT_MODEL = (By.ID, 'input-model')
    DATA_TAB = (By.XPATH, "//*[contains(text(), 'Data')]")
    ALL_PRODUCTS = (By.NAME, 'selected[]')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.open('/admin')

    def login(self):
        self._fill_input(self.LOGIN, 'admin')
        self._fill_input(self.PASSWORD, 'admin')
        self._click(self.SUBMIT)

    def open_products(self):
        self._click(self.CATALOG)
        self._click(self.PRODUCTS)

    def add_new_product(self):
        self._click(self.ADD_PRODUCT)

    def fill_product_card(self, product_name: str, tag_title: str, product_model: str):
        self._fill_input(self.PRODUCT_NAME, product_name)
        self._fill_input(self.TAG_TITLE, tag_title)
        self._click(self.DATA_TAB)
        self._fill_input(self.PRODUCT_MODEL, product_model)
        self._click(self.SUBMIT)

    def select_product_from_catalog(self):
        elements = self._elements_by_selector(self.ALL_PRODUCTS)
        el = random.choice(elements)
        self._click_element(el)

    def delete_product(self):
        self._click(self.DELETE_PRODUCT)
