import helpers

from page_object.AdminPage import AdminPage
from page_object.RegisterPage import RegisterPage
from page_object.elements.SuccessAlertElement import SuccessAlert
from page_object.elements.HeaderElement import HeaderElement
from page_object.elements.BasketElement import BasketElement


def test_user_register(browser, new_user):
    register = RegisterPage(browser)
    register.fill_form(**new_user)
    text = register.get_success_text()
    assert text == 'Your Account Has Been Created!', 'Text message not equal to expected'


def test_switch_currency_to_pound(browser):
    HeaderElement(browser).click_on_currency_list()
    HeaderElement(browser).click_on_pound()
    text = BasketElement(browser).get_basket_text()
    assert "£" in text, 'Text message not equal to expected'


def test_add_new_product_to_catalog(browser):
    admin_page = AdminPage(browser)
    admin_page.login()
    admin_page.open_products()
    admin_page.add_new_product()
    admin_page.fill_product_card(product_name='Testing product_' + helpers.get_timestamp(),
                                 tag_title='Testing tag',
                                 product_model='Testing model')
    text = SuccessAlert(browser).get_text_from_alert()
    assert 'Success: You have modified products!' in text, 'Text message not equal to expected'


def test_delete_product_from_catalog(browser):
    admin_page = AdminPage(browser)
    admin_page.login()
    admin_page.open_products()
    admin_page.select_product_from_catalog()
    admin_page.delete_product()
    admin_page.accept_alert()
    text = SuccessAlert(browser).get_text_from_alert()
    assert 'Success: You have modified products!' in text, 'Text message not equal to expected'
