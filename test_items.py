import time


def test_check_button_is_on_the_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button, "button is not found"