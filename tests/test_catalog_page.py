from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_content_title(browser):
    browser.get(browser.url + '/smartphone')
    wait = WebDriverWait(browser, 10)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#content > h2')))
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#content > h2'), 'Phones & PDAs'))
    assert el.text == 'Phones & PDAs'


def test_sort_by(browser):
    browser.get(browser.url + '/smartphone')
    wait = WebDriverWait(browser, 10)
    dropdown = Select(wait.until(EC.visibility_of_element_located((By.ID, 'input-sort'))))
    assert len(dropdown.options) == 9


def test_show_page_num(browser):
    browser.get(browser.url + '/smartphone')
    wait = WebDriverWait(browser, 10)
    dropdown = Select(wait.until(EC.visibility_of_element_located((By.ID, 'input-limit'))))
    assert len(dropdown.options) == 5


def test_product_title(browser):
    browser.get(browser.url + '/smartphone')
    el = browser.find_elements_by_css_selector('.caption')
    assert 'HTC Touch HD' in el[0].text


def test_product_compare_count(browser):
    browser.get(browser.url + '/smartphone')
    wait = WebDriverWait(browser, 10)
    el = wait.until(EC.visibility_of_element_located((By.ID, 'compare-total')))
    assert el.text == 'Product Compare (0)'
