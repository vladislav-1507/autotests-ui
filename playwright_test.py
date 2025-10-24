from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until="networkidle",  # Ждем полной загрузки страницы
    )

    registration_link = page.get_by_test_id("login-page-registration-link")
    registration_link.hover()

    page.wait_for_timeout(5000)

    # with page.expect_request("**/*logo*.png") as first:
    #     page.goto("https://wikipedia.org")
    # print(first.value.url)

    # with page.expect_popup() as popup:
    #     page.get_by_text("open the popup").click()
    # popup.value.goto("https://wikipedia.org")