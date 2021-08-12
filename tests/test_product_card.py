from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_breadcrumb(browser):
    browser.get(browser.url + '/macbook')
    wait = WebDriverWait(browser, 10)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.breadcrumb')))
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.breadcrumb'), 'MacBook'))
    assert el.text == 'MacBook'


def test_add_to_card(browser):
    browser.get(browser.url + '/macbook')
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.ID, 'button-cart'))).click()
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.alert-success')))
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.alert-success'), 'Success: You have added'))
    assert 'Success: You have added MacBook to your shopping cart!' in el.text


def test_card_total(browser):
    browser.get(browser.url + '/macbook')
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#cart > button')))


def test_search_btn(browser):
    browser.get(browser.url + '/macbook')
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-default'))).click()
    assert browser.current_url == browser.url + '/index.php?route=product/search'


def test_description_block(browser):
    browser.get(browser.url + '/macbook')
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.tab-content')))
