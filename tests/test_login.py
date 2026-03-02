import pytest
from pages.login_page import LoginPage

class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        # This attaches the page object to the class instance (self)
        self.login_page = LoginPage(driver)
        self.driver = driver

# Verify login with wrong username & wrong password
    def test_002(self, driver):
        self.login_page.click_pom()
        self.login_page.set_user_name("aaa")
        self.login_page.set_password("aaa")
        self.login_page.click_login_button()
        # Capture error message
        assert self.login_page.is_alert_present() == True
        assert self.login_page.alert_message_text() == '⚠️ Invalid username or password. Please try again.'