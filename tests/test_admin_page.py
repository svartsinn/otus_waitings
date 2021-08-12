from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def test_panel_links(browser):
    browser.get(browser.admin_url)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.ID, 'navipanellinks')))


def test_top_menu_container(browser):
    browser.get(browser.admin_url)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.menucontainer')))


def test_lang_settings(browser):
    browser.get(browser.admin_url)
    wait = WebDriverWait(browser, 10)
    dropdown = Select(wait.until(EC.visibility_of_element_located((By.ID, 'sel-lang'))))
    assert len(dropdown.options) == 44


def test_drop_list(browser):
    browser.get(browser.admin_url)
    el = browser.find_elements_by_css_selector('.drop_list')
    assert len(el) == 2


def test_doc_container(browser):
    browser.get(browser.admin_url)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.ID, 'maincontainer')))
