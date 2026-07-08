from apps.demo_web.page_model import LoginPage

class FakeDriver:
    def __init__(self):
        self.values = {}
        self.clicked = []
    def type(self, selector, value):
        self.values[selector] = value
    def click(self, selector):
        self.clicked.append(selector)
    def text(self, selector):
        return "Invalid username or password"

def test_login_page_object_smoke_flow():
    driver = FakeDriver()
    page = LoginPage(driver)
    page.login("qa@example.test", "bad-password")
    assert driver.values[LoginPage.username] == "qa@example.test"
    assert LoginPage.submit in driver.clicked
    assert "Invalid" in page.error_text()
