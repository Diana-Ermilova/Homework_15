import pytest
from selene import browser, have


@pytest.fixture(params=[(1920, 1080), (1024, 1366)])
def browser_setup(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width > 1024:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()


def test_github_desktop(browser_setup):
    if browser_setup == "mobile":
        pytest.skip("skip desktop")
    browser.open("https://github.com/")
    browser.all('button').element_by(have.text('Sign up')).click()


def test_github_mobile(browser_setup):
    if browser_setup == "desktop":
        pytest.skip("skip mobile")
    browser.open("https://github.com/")
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-up').click()