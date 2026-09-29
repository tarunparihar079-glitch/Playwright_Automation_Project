import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),      
    ("locked_out_user", "secret_sauce"),    
    ("problem_user", "secret_sauce")   
])

def test_multiple_logins(page: Page, username, password):
    print(f"\n---> Test run for this user: {username}")

    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login(username, password)