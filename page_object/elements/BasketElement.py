from ..BasePage import BasePage
from selenium.webdriver.common.by import By


class BasketElement(BasePage):
    BASKET = (By.ID, 'cart-total')

    def verify_basket_element(self):
        return self._is_element_presence(self.BASKET)

    def get_basket_text(self):
        return self._get_element_text(self.BASKET)
