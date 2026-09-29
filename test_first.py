from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto("https://www.instagram.com")

    print("Page Title is:", page.title())
    assert "Instagram" in page.title()

    browser.close()