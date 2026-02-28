import pytest
from pages.login_page import LoginPage

class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        # This attaches the page object to the class instance (self)
        self.login_page = LoginPage(driver)
        self.driver = driver

    # Testcase to verify redirection url
    def test_001(self, driver):
        self.login_page.click_pom()
        # Verify url
        current_url = self.login_page.get_current_page_url()
        expected_url = "https://www.qaplayground.com/bank"
        assert current_url == expected_url

    # Verify login with wrong username & wrong password
    def test_002(self, driver):
        self.login_page.click_pom()
        self.login_page.set_user_name("aaa")
        self.login_page.set_password("aaa")
        self.login_page.click_login_button()
        # Capture error message
        assert self.login_page.is_alert_present() == True
        assert self.login_page.alert_message_text() == '⚠️ Invalid username or password. Please try again.'

    # Verify login with wrong username & correct password
    def test_003(self, driver):
        self.login_page.click_pom()
        self.login_page.set_user_name("aaa")
        self.login_page.set_password("admin123")
        self.login_page.click_login_button()
        # Capture error message
        assert self.login_page.is_alert_present() == True
        assert self.login_page.alert_message_text() == '⚠️ Invalid username or password. Please try again.'

    # Verify login with correct username & wrong password
    def test_004(self, driver):
        self.login_page.click_pom()
        self.login_page.set_user_name("admin")
        self.login_page.set_password("admin")
        self.login_page.click_login_button()
        # Capture error message
        assert self.login_page.is_alert_present() == True
        assert self.login_page.alert_message_text() == '⚠️ Invalid username or password. Please try again.'

    # Verify login with correct username &  password
    def test_005(self, driver):
        self.login_page.click_pom()
        self.login_page.set_user_name("admin")
        self.login_page.set_password("admin123")
        self.login_page.click_login_button()
        # Step 3: Verify url
        current_url = self.login_page.get_current_page_url()
        expected_url = "https://www.qaplayground.com/bank/dashboard"
        assert current_url == expected_url

