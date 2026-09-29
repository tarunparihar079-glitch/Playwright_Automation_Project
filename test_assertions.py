from playwright.sync_api import Page,expect

def test_dyn_ele(page : Page):
    page.goto("https://demoqa.com/dynamic-properties")

    enable_btn = page.locator("#enableAfter")
    expect(enable_btn).to_be_enabled(timeout=10000)
    print("Button is enabled")

    visible_btn = page.locator("#visibleAfter")
    expect(visible_btn).to_be_visible()
    print("Button is visible")

    visible_btn.click()