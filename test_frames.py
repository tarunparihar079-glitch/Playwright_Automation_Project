from playwright.sync_api import Page,expect

def test_frames(page:Page):
    page.goto("https://demoqa.com/frames")

    frame1_text = page.frame_locator("#frame1").locator("#sampleHeading").inner_text()
    print(F"\nFrame1 Text:{frame1_text}")

    frame2_text = page.frame_locator("#frame2").locator("#sampleHeading").inner_text()
    print(f"\nFrame2 Text:{frame2_text}")