from playwright.sync_api import Page,expect
from pages.login_page import LoginPage

def test_save_session(page:Page):
    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)
    login_page.login("standard_user","secret_sauce")

    page.context.storage_state(path="auth.json")
    print(f"\nSession file auth.json saved")

def test_direct_dashboard(browser):
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()

    page.goto("https://www.saucedemo.com/inventory.html")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    print("\nWithout login direct inventory")