from playwright.sync_api import Page,expect
import re

def test_tabs(page:Page):
    page.goto("https://demoqa.com/browser-windows")

    with page.context.expect_page() as new_page_info:
        page.locator("#tabButton").click()

    new_page = new_page_info.value
    new_page.wait_for_load_state()

    heading_text = new_page.locator("#sampleHeading").inner_text()
    print(f"\nNew Tab Text: {heading_text}")   

    # expect(new_page).to_have_url(re.compile("sample")) 