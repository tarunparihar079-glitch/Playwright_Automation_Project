from playwright.sync_api import Page,expect
from pages.login_page import LoginPage
import os
from dotenv import load_dotenv

load_dotenv()

def test_valid_login(page:Page):
    page.goto(os.getenv("BASE_URL"))

    login_page = LoginPage(page)
    login_page.login(os.getenv("TEST_USER"),os.getenv("TEST_PASS"))

    expect(page).to_have_url(f"{os.getenv('BASE_URL')}inventory.html")