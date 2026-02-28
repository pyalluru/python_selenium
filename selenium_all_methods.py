import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Add arguments & set Capabilities
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--start-maximized")                           # Open browser maximized
options.add_argument("--incognito")                                 # Open in incognito mode
options.add_argument("--disable-popup-blocking")                    # Disable Popup blocking
options.add_argument("--headless")                                  # Run without UI
options.add_argument("--disable-gpu")
options.add_extension("/path/to/extension.crx")                     # Add Chrome extension
options.set_capability("acceptInsecureCerts", True)     # Allow insecure SSL certs

# Launch driver
chrome_driver_path = os.path.join(os.getcwd(), "drivers\chrome\chromedriver.exe")
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Open url
driver.get("url")                       # Open url
current_url = driver.current_url
title = driver.title
page_source = driver.page_source

# Open Browser window
driver.get_window_size()                # To get window size
driver.maximize_window()                # To maximize the window
driver.minimize_window()                # To Minimize the window
driver.set_window_size(1090, 650)       # To set custom size of window

# Navigations
driver.back()                           # Back Navigation
driver.forward()                        # forward
driver.refresh()                        # Refresh

# Find elements
driver.find_element(By.XPATH, "//xpath")    # Find one element
driver.find_elements(By.XPATH, "//xpath")    # Find All element

# Implicit Wait, NoSuchElementException
driver.implicitly_wait(10)
# Explicit wait, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
element1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//xpath")))
# Fluent Wait, Almost same a explicit but with poll_frequency, TimeoutException
element2 = WebDriverWait(driver, 10, poll_frequency=2).until(EC.presence_of_element_located((By.XPATH, "//xpath")))
# List of expected conditions in explicit wait
presence_of_element_located = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//xpath")))
visibility_of_element_located = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//xpath")))
element_to_be_clickable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//xpath")))
text_to_be_present_in_element = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//xpath"), "text"))

# Element Actions
element = driver.find_element("id", "example-id")
element.clear()
element.click()
element.send_keys("Helloooo")
element.send_keys(Keys.ENTER)            # pass buttons, need to import Keys module
element.get_attribute("attribute_name")
element.screenshot("element_screenshot.png")        # Specific element screen shot
driver.save_screenshot("screenshot.png")            # full page screenshot

# Element Status (Boolean values)
element = driver.find_element("id", "example-id")
text = element.text
element.is_displayed()
element.is_enabled()
element.is_selected()

# Working with Alert
alert = driver.switch_to.alert
alert.accept()
alert.dismiss()
alert.send_keys("Helloooo")
alert.send_keys(Keys.ENTER)

# Select Class (Dropdowns) (Single selection & multi selection)
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element("id", "dropdown-id"))
all_options = select.options                            # Get all options from dropdown
first_selected_options = select.first_selected_option   # Get first selected option
all_selected_options = select.all_selected_options      # get all selected options
select.select_by_index(0)                               # Select one
select.select_by_value("value")
select.select_by_visible_text("option text")
select.deselect_by_index(0)                             # Deselect one
select.deselect_by_value("value")
select.deselect_by_visible_text("option text")
select.deselect_all()                                   # deselect all

# Working with multiple windows or tabs or window handles
handles = driver.window_handles             # Get all windows
driver.switch_to.window(handles[1])         # Go to another window
driver.switch_to.window(handles[0])         # Back to previous window

# Iframes
driver.switch_to.frame(0)                   # Switch using index
driver.switch_to.frame("Frame_id")          # Switch using frame id
driver.switch_to.frame(element)             # Switch using element
driver.switch_to.default_content()          # Switch out from iframe
driver.switch_to.parent_frame()             # Go one level up, if frames inside frame ..etc

# Cookies
all_cookies = driver.get_cookies()                  # To get all cookies
one_cookie = driver.get_cookie("cookie_name")       # To get one cookie
example_cookie = { "name": "myCookie", "value": "cookie_value", "domain": "example.com", "path": "/", "secure": False, "httpOnly": False }
driver.add_cookie(example_cookie)                   # To add one cookie
driver.delete_cookie("myCookie")
driver.delete_all_cookies()

# Scrolling pages
driver.execute_script("window.scrollBy(0, 500);")                               # Scroll down 500px
driver.execute_script("window.scrollBy(0, -500);")                              # Scroll up 500px
driver.execute_script("window.scrollBy(500, 0);")                               # Scroll right 500px
driver.execute_script("window.scrollBy(-500, 0);")                              # Scroll left 500px
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")        # Scroll to bottom
driver.execute_script("window.scrollTo(0, 0);")                                 # Scroll to top
driver.execute_script("arguments[0].scrollIntoView();", element)                # Scroll to element

# ActionChains class
from selenium.webdriver.common.action_chains import ActionChains
element = driver.find_element("id", "myElement")
actions = ActionChains(driver)
actions.click(element).perform()                                                # Click
actions.context_click(element).perform()                                        # Context click right click
actions.double_click(element).perform()                                         # Double click
actions.drag_and_drop(element1, element2).perform()                             # Drag element 1 to element 2
actions.click_and_hold(element1).move_to_element(element2).release().perform()  # Drag element 1 to element 2
actions.click_and_hold(element).pause(2).release().perform()                    # Click and hold element for 2 seconds

