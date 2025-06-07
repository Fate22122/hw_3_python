from selene import browser, have


def test_search(browser_info):
    browser.element('[name="q"]').type('qrqrqrqrq5vghje').press_enter()
    browser.element('html').should(have.text('No results found for qrqrqrqrq5vghje'))