from selene import browser, have


def test_search(browser_info):
    browser.element('[name="q"]').type('moex.com').press_enter()
    browser.element('html').should(have.text('Moex'))