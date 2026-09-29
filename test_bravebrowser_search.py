# from playwright.sync_api import Page,expect

# def test_search_on_bb(page:Page):
#     page.goto("https://search.brave.com/?lang=en-in")
#     page.get_by_role("searchbox",name="Search Brave Browser").fill("Instagram")
#     page.get_by_role("button",name="Search").click()
#     heading = page.locator("h1")
#     expect(heading).to_contain_text("Instagram")
import re
from playwright.sync_api import Page, expect

def test_search_on_bb(page: Page):
    # 1. Brave search page par jao
    page.goto("https://search.brave.com/?lang=en-in")
    
    # 2. Exact ID (#searchbox) ka use karke locate aur type karo
    search_input = page.locator("#searchbox")
    search_input.fill("Instagram")
    
    # 3. Enter press karo (Brave par alag se search button click karne se best yahi he)
    search_input.press("Enter")
    s_input = page.get_by_text("Instagram", exact=True).first
    s_input.click()
    
    # 4. Verify karo ki naye khule hue page ke title me 'Instagram' he
    expect(page).to_have_title(re.compile("Instagram", re.IGNORECASE))