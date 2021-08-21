from page_object.CatalogPage import CatalogPage


def test_content_title(browser):
    text = CatalogPage(browser).get_title_text()
    assert text == 'Phones & PDAs', 'Text message not equal to expected'


def test_sort_by(browser):
    dropdown_len = CatalogPage(browser).count_dropdown_list()
    assert dropdown_len == 9, 'Dropdown list has an incorrect number of elements'


def test_show_page_num(browser):
    page_number = CatalogPage(browser).count_page_numbers()
    assert page_number == 5, 'Dropdown list has an incorrect number of elements'


def test_product_title(browser):
    text = CatalogPage(browser).get_caption_text()
    assert 'HTC Touch HD' in text, 'Text message not equal to expected'


def test_product_compare_count(browser):
    text = CatalogPage(browser).get_compare_text()
    assert text == 'Product Compare (0)', 'Text message not equal to expected'
