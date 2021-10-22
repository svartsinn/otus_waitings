import time

import allure

from page_object.ProductPage import ProductPage
from page_object.elements.SearchElement import SearchElement


@allure.title("Название хлебных крошек на странице")
def test_breadcrumb(driver):
    product = ProductPage(driver)
    product.verify_breadcrumb_element()
    text = product.get_breadcrumb_text()
    assert text == 'MacBook', 'Text message not equal to expected'


@allure.title("Добавление ноутбука в корзину")
def test_add_to_card(driver):
    product = ProductPage(driver)
    product.click_button_card_element()
    text = product.get_alert_text()
    assert 'Success: You have added MacBook to your shopping cart!' in text, \
        'Text message not equal to expected'


@allure.title("Общее количество продуктов на странице")
def test_card_total(driver):
    ProductPage(driver).verify_card_total_element()


@allure.title("Переход на URL после нажатия на поиск")
def test_url_after_click_search_button(driver):
    ProductPage(driver)
    search = SearchElement(driver)
    search.click_on_search_button()
    url = search.get_current_url()
    assert '/index.php?route=product/search' in url, 'Current URL not equal to expected'


@allure.title("Проверка блока с описанием")
def test_description_block(driver):
    ProductPage(driver).verify_description_element()
