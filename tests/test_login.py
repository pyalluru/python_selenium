import pytest
from pages.login_page import LoginPage

class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        # This attaches the page object to the class instance (self)
        self.login_page = LoginPage(driver)
        self.driver = driver

