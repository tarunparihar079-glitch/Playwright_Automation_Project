from playwright.sync_api import Page, expect

def test_fill_form(page:Page):
    page.goto("https://demoqa.com/automation-practice-form")
    page.locator("#firstName").fill("Tarun")
    page.locator("#lastName").fill("Parihar")
    page.locator("#userEmail").fill("udfeuifyiua123@gmail.com")
    page.locator("label[for='gender-radio-1']").click()
    page.locator("#userNumber").fill("9690901041")
    page.locator("#subjectsInput").fill("Hindi,English")
    page.locator("label[for='hobbies-checkbox-3']").check()
    page.locator("#uploadPicture").set_input_files("demo.pdf")
    page.locator("#currentAddress").fill("Jaipur,Rajasthan")
    page.locator("#state").click()
    page.locator("#react-select-3-input").fill("Rajasthan")
    page.locator("#react-select-3-input").press("Enter")
    page.locator("#city").click()
    page.locator("#react-select-4-input").fill("Jaipur")

