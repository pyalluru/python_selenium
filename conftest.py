import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    # Setup
    # Replace with your actual ChromeDriver path
    chrome_driver_path = os.path.join(os.getcwd(), "drivers\chrome\chromedriver.exe")
    # Setup Chrome driver using your path
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    print("====== TestCase Execution Started. ========")
    # Step 1: Open the practice site
    driver.get("https://www.qaplayground.com/practice")
    driver.maximize_window()
    print("✅ Opened site & Maximised successfully")
    time.sleep(3)

    yield driver  # This is where the test runs

    # Cleanup
    driver.quit() # Cleanup after the test