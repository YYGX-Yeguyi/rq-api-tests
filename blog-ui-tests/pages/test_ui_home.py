#测试页面是否正常渲染
from playwright.sync_api import sync_playwright, expect

def test_home_shows_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)   # headless=False 能看到浏览器
        page = browser.new_page()
        page.goto("http://localhost:5173")
        expect(page.locator("text=WhiteAbyss")).to_be_visible()
        browser.close()