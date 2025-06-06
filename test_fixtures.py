import pytest
from selene import browser, have


@pytest.fixture(params=[(1920, 1080), (1366, 768)])
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[(1024, 1366), (430, 932)])
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


def test_github_desktop(desktop_browser):
    browser.open("https://github.com/")
    browser.all('button').element_by(have.text('Sign up')).click()


def test_github_mobile(mobile_browser):
    browser.open("https://github.com/")
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-up').click()