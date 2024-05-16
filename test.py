import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.bKash.customerapp',
    appActivity='.MainActivity',
    noReset= True,
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))

    
    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
    
    def test_enter_app(self, pin = "99805"):
        # Typing pin and proceed
        for digit in pin:
            key_element = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=digit)
            key_element.click()
        # Waiting enabling Proceed button
        self.driver.implicitly_wait(5)
        # clicking the Proceed
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="পরবর্তী"]').click()
        # Wainting to load the main screen
        self.driver.implicitly_wait(30)
    
    
    def test_check_balance(self):
        # Click on the check balance
        # self.enter_app("99805")
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="ব্যালেন্স দেখুন"]').click()
        self.driver.implicitly_wait(5)

    # def test_find_battery(self) -> None:
    #     el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    #     el.click()

if __name__ == '__main__':
    unittest.main()