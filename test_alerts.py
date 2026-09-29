from playwright.sync_api import Page,expect

def test_alert(page:Page):
    page.goto("https://demoqa.com/alerts")

    def handle_dialog(dialog):
        print(f"\nPopup text:{dialog.message}")
        dialog.accept()

    page.on("dialog",handle_dialog)

    page.locator("#alertButton").click()    