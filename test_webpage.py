from selenium import webdriver
import time

def test_ig():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://www.instagram.com')
    assert driver.title == "Instagram"
    time.sleep(5) 
    driver.quit()

def test_google():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://www.google.com')
    assert driver.title == "Google"
    driver.quit()

def test_fb():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://www.facebook.com')
    assert driver.title == "Facebook"
    driver.quit()