import pytest
from selene import browser, by


@pytest.fixture(params=[(1920, 1080), (1024, 1366)])
def browser_setup(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.mark.parametrize("browser_setup", [(1920, 1080)], indirect=True)
def test_github_desktop(browser_setup):
    browser.open("http://github.com")
    browser.element(by.text("Sign up")).click()


@pytest.mark.parametrize("browser_setup", [(1024, 1366)], indirect=True)
def test_github_mobile(browser_setup):
    browser.open("https://github.com/")
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-up').click()