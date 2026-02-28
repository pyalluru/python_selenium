import time

from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Actions
    def click_pom(self):
        # Step 2: Click on POM & Verify new url
        time.sleep(1)
        pom_element_path = '//span[text() = "Page Object Model"]'
        pom_element = self.driver.find_element(By.XPATH, pom_element_path)
        pom_element.click()
        time.sleep(2)
        print("✅ Clicked on POM successfully")

    def set_user_name(self, use_name_value):
        self.driver.find_element(By.ID, 'username').send_keys(use_name_value)
        time.sleep(1)

    def set_password(self, password_value):
        self.driver.find_element(By.ID, 'password').send_keys(password_value)
        time.sleep(1)

    def click_login_button(self):
        self.driver.find_element(By.ID, 'login-btn').click()
        time.sleep(1)

    def is_alert_present(self):
        status = False
        element = self.driver.find_element(By.ID, 'alert-message')
        if element:
            status = True
        return status

    def alert_message_text(self):
        text = ""
        element = self.driver.find_element(By.ID, 'alert-message')
        if element:
            text = element.text
        else:
            text = None
        return text

    def get_current_page_url(self):
        return self.driver.current_url