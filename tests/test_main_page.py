from page_object.elements.BasketElement import BasketElement
from page_object.elements.FooterElement import FooterElement
from page_object.elements.SearchElement import SearchElement
from page_object.MainPage import MainPage


def test_title(browser):
    basket = BasketElement(browser)
    basket.verify_basket_element()
    assert '$0.00' in basket.get_basket_text(), 'Text message not equal to expected'


def test_search_button(browser):
    search = SearchElement(browser)
    search.submit_query_to_search('Test query')
    search.verify_search_result()
    text = search.get_search_result_text()
    assert text == 'Search - Test query', 'Text message not equal to expected'


def test_featured_title(browser):
    assert MainPage(browser).get_title_text() == 'Featured', 'Text message not equal to expected'


def test_image_count(browser):
    assert MainPage(browser).count_image_on_page() == 4


def test_footer_element(browser):
    FooterElement(browser).verify_footer_element()
