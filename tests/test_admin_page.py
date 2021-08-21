from page_object.PHPMyAdminPage import PHPMyAdminPage


def test_panel_links(browser):
    PHPMyAdminPage(browser).verify_panel_element()


def test_top_menu_container(browser):
    PHPMyAdminPage(browser).verify_menu_element()


def test_count_lang_dropdown_list(browser):
    dropdown_list = PHPMyAdminPage(browser).count_dropdown_list()
    assert dropdown_list == 44


def test_drop_list(browser):
    drop_list = PHPMyAdminPage(browser).count_elements()
    assert drop_list == 2


def test_doc_container(browser):
    PHPMyAdminPage(browser).verify_doc_element()
