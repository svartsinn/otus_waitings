from page_object.ProductPage import ProductPage
from page_object.elements.SearchElement import SearchElement


def test_breadcrumb(browser):
    product = ProductPage(browser)
    product.verify_breadcrumb_element()
    text = product.get_breadcrumb_text()
    assert text == 'MacBook', 'Text message not equal to expected'


def test_add_to_card(browser):
    product = ProductPage(browser)
    product.click_button_card_element()
    text = product.get_alert_text()
    assert 'Success: You have added MacBook to your shopping cart!' in text, \
        'Text message not equal to expected'


def test_card_total(browser):
    ProductPage(browser).verify_card_total_element()


def test_url_after_click_search_button(browser):
    search = SearchElement(browser)
    search.click_on_search_button()
    url = search.get_current_url()
    assert '/index.php?route=product/search' in url, 'Current URL not equal to expected'


def test_description_block(browser):
    ProductPage(browser).verify_description_element()
