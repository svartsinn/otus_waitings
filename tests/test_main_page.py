import allure

from page_object.elements.BasketElement import BasketElement
from page_object.elements.FooterElement import FooterElement
from page_object.elements.SearchElement import SearchElement
from page_object.MainPage import MainPage


@allure.title("Текст суммы для пустой корзины")
def test_empty_basket_amount(driver):
    MainPage(driver)
    basket = BasketElement(driver)
    basket.verify_basket_element()
    assert '$0.00' in basket.get_basket_text(), 'Text message not equal to expected'


@allure.title("Поисковая выдача по запросу")
def test_search_query_result(driver):
    MainPage(driver)
    search = SearchElement(driver)
    search.submit_query_to_search('Test query')
    search.verify_search_result()
    text = search.get_search_result_text()
    assert text == 'Search - Test query', 'Text message not equal to expected'


@allure.title("Заголовок блока Featured")
def test_featured_title(driver):
    assert MainPage(driver).get_title_text() == 'Featured', 'Text message not equal to expected'


@allure.title("Количество изображений на странице")
def test_image_count(driver):
    assert MainPage(driver).count_image_on_page() == 4


@allure.title("Наличие футера на странице")
def test_verify_footer(driver):
    MainPage(driver)
    FooterElement(driver).verify_footer_element()
