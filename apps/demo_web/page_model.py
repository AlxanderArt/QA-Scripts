class LoginPage:
    username = "[data-testid='username']"
    password = "[data-testid='password']"
    submit = "[data-testid='submit-login']"
    error = "[data-testid='login-error']"

    def __init__(self, driver):
        self.driver = driver

    def login(self, username: str, password: str):
        self.driver.type(self.username, username)
        self.driver.type(self.password, password)
        self.driver.click(self.submit)

    def error_text(self) -> str:
        return self.driver.text(self.error)
