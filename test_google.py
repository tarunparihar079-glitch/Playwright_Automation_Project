import pytest
from selenium import webdriver

# 1. Fixture: Setup aur Teardown ka kaam karega (Dono browsers ke liye)
@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    # Browser check aur open karna
    if request.param == "chrome":
        driver = webdriver.Chrome()   # Naya modern tarika (No Manager needed)
    elif request.param == "firefox":
        driver = webdriver.Firefox()  # Naya modern tarika
    
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://www.google.com")
    
    # Class (self) ke andar driver ko set kar rahe hain
    request.cls.driver = driver
    
    yield  # Har ek test yahan aakar execute hoga
    
    # Har test cycle ke baad browser close karna
    driver.quit()


# 2. Base Class: Jisme humne upar wala fixture laga diya
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


# 3. Test Class: Har test case yahan likhenge
class Test_Google(BaseTest):
    
    def test_google_title(self):
        # self.driver likhne se automatically open browser mil jayega
        assert self.driver.title == "Google"

    def test_google_url(self):
        assert "google.com" in self.driver.current_url