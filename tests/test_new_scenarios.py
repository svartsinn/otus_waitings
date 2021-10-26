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
