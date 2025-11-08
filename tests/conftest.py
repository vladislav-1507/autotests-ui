# import pytest
# from playwright.sync_api import sync_playwright, Page


# @pytest.fixture
# def chromium_page() -> Page:  # type: ignore
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         yield browser.new_page()
#         browser.close() # для наглядности(браузер закроется в любом случае)


import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()