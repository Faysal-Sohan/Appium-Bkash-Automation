from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_caps = {
    "platformName": "Android",
    "deviceName": "your_device_name",
    "appPackage": "com.bKash.customerapp",
    "appActivity": ".MainActivity",
    "automationName": "UIAutomator2",
    "noReset": True
}

# Start the Appium server with appium --allow-insecure chromedriver_autodownload
appium_server_url = 'http://127.0.0.1:4723/wd/hub'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))

driver.implicitly_wait(10)

pin = "99805"

# Find and press the keys on the keypad
for digit in pin:
    key_element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value=digit)
    key_element.click()

driver.implicitly_wait(10)
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="পরবর্তী"]').click()
driver.implicitly_wait(10)

# Click on the balance button or navigate to the balance section
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="ব্যালেন্স দেখুন"]').click()

# Wait for the balance to load
time.sleep(10)

# Close the app
driver.quit()
