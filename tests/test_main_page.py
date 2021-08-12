from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_title(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 10)
    el = wait.until(EC.visibility_of_element_located((By.ID, 'cart-total')))
    assert '$0.00' in el.text


def test_search_button(browser):
    browser.get(browser.url)
    search_field = browser.find_element_by_name('search')
    search_field.send_keys('Test query')
    browser.find_element_by_css_selector('.btn-default').click()
    element = browser.find_element_by_css_selector('#content > h1')
    assert 'Search - Test query' == element.text


def test_featured_title(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 10)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#content > h3')))
    assert el.text == 'Featured'


def test_image_count(browser):
    browser.get(browser.url)
    el = browser.find_elements_by_css_selector('.image')
    assert len(el) == 4


def test_footer_element(browser):
    browser.get(browser.url)
    browser.find_element_by_xpath("//*[contains(text(), 'My Account')]")
