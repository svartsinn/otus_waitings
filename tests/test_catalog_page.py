import allure

from page_object.CatalogPage import CatalogPage


@allure.title("Заголовок страницы")
def test_content_title(driver):
    text = CatalogPage(driver).get_title_text()
    assert text == 'Phones & PDAs', 'Text message not equal to expected'


@allure.title("Элементы выпадающего списка с сортировкой")
def test_sort_by_list(driver):
    dropdown_len = CatalogPage(driver).count_dropdown_list()
    assert dropdown_len == 9, 'Dropdown list has an incorrect number of elements'


@allure.title("Общее количество продуктов на странице")
def test_show_page_num(driver):
    page_number = CatalogPage(driver).count_page_numbers()
    assert page_number == 5, 'Dropdown list has an incorrect number of elements'


@allure.title("Заголовок для продукта")
def test_product_title(driver):
    text = CatalogPage(driver).get_caption_text()
    assert 'HTC Touch HD' in text, 'Text message not equal to expected'


@allure.title("Заголовок элемента сравнения продуктов")
def test_product_compare_count(driver):
    text = CatalogPage(driver).get_compare_text()
    assert text == 'Product Compare (0)', 'Text message not equal to expected'
