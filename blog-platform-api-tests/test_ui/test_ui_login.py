from playwright.sync_api import sync_playwright, expect


def test_admin_login():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("http://localhost:5173/login")
        page.get_by_role("textbox", name="用户名").fill("admin")
        page.get_by_role("textbox", name="密码").fill("123456")
        page.get_by_role("button", name="登 录").click()

        expect(page).to_have_url("http://localhost:5173/admin")

        browser.close()






