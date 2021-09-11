import allure

from page_object.PHPMyAdminPage import PHPMyAdminPage


@allure.title("Наличие панели со ссылками")
def test_panel_links(driver):
    PHPMyAdminPage(driver).verify_panel_element()


@allure.title("Верхнее меню со ссылками")
def test_top_menu_container(driver):
    PHPMyAdminPage(driver).verify_menu_element()


@allure.title("Количество элементов в языковом меню")
def test_count_lang_dropdown_list(driver):
    dropdown_list = PHPMyAdminPage(driver).count_dropdown_list()
    assert dropdown_list == 44


@allure.title("Выпадающий список")
def test_drop_list(driver):
    drop_list = PHPMyAdminPage(driver).count_elements()
    assert drop_list == 2


@allure.title("Меню с документами")
def test_doc_container(driver):
    PHPMyAdminPage(driver).verify_doc_element()
