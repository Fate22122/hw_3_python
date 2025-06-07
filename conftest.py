import pytest
from selene import browser

@pytest.fixture()
def browser_info():
    browser.open('https://duckduckgo.com/')
    browser.config.window_width = 1000
    browser.config.window_height = 780
    yield
    browser.quit()