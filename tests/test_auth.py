from playwright.sync_api import Page,expect
from pages.login_page import LoginPage
import os
from dotenv import load_dotenv

load_dotenv()

def test_save_session(page:Page):
    page.goto(os.getenv("BASE_URL").strip())

    login_page = LoginPage(page)
    login_page.login(os.getenv("TEST_USER"),os.getenv("TEST_PASS"))

    page.context.storage_state(path="auth.json")
    print(f"\nSession file auth.json saved")

def test_direct_dashboard(browser):
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()

    page.goto(f"{os.getenv('BASE_URL').strip()}inventory.html")

    expect(page).to_have_url(f"{os.getenv('BASE_URL').strip()}inventory.html")
    print("\nWithout login direct inventory")