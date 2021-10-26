import allure
import pytest

import helpers

from page_object.AdminPage import AdminPage
from page_object.RegisterPage import RegisterPage
from page_object.elements.SuccessAlertElement import SuccessAlert
from page_object.elements.HeaderElement import HeaderElement
from page_object.elements.BasketElement import BasketElement


@allure.title("Регистрация нового пользователя")
def test_user_register(driver, new_user):
    register = RegisterPage(driver)
    register.fill_form(**new_user)
    text = register.get_success_text()
    assert text == 'Your Account Has Been Created!', 'Text message not equal to expected'


@allure.title("Переключение на фунты")
def test_switch_currency_to_pound(driver):
    RegisterPage(driver)
    HeaderElement(driver).click_on_currency_list()
    HeaderElement(driver).click_on_pound()
    text = BasketElement(driver).get_basket_text()
    assert "£" in text, 'Text message not equal to expected'


@allure.title("Добавление нового продукта в каталог")
def test_add_new_product_to_catalog(driver):
    """
    By default Opencart use predefined password for admin user therefore this test failure
    """
    admin_page = AdminPage(driver)
    admin_page.login()
    admin_page.open_products()
    admin_page.add_new_product()
    admin_page.fill_product_card(product_name='Testing product_' + helpers.get_timestamp(),
                                 tag_title='Testing tag',
                                 product_model='Testing model')
    text = SuccessAlert(driver).get_text_from_alert()
    assert 'Success: You have modified products!' in text, 'Text message not equal to expected'


@allure.title("Удаление продукта из каталога")
def test_delete_product_from_catalog(driver):
    admin_page = AdminPage(driver)
    admin_page.login()
    admin_page.open_products()
    admin_page.select_product_from_catalog()
    admin_page.delete_product()
    admin_page.accept_alert()
    text = SuccessAlert(driver).get_text_from_alert()
    assert 'Success: You have modified products!' in text, 'Text message not equal to expected'
