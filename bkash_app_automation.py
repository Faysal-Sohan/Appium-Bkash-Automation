from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

class BkashAppAutomation:
    def __init__(self):
        self.desired_caps = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName='Android',
            appPackage='com.bKash.customerapp',
            appActivity='.MainActivity',
            noReset= True,
            language='en',
            locale='US'
        )
        self.appium_server_url = 'http://127.0.0.1:4723'
        self.driver = None
    
    
    def start_app(self):
        self.driver = webdriver.Remote(self.appium_server_url, options=UiAutomator2Options().load_capabilities(self.desired_caps))
        self.driver.implicitly_wait(30)
    
    
    def enter_app(self, pin: str):
        # Typing pin and proceed
        for digit in pin:
            key_element = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=digit)
            key_element.click()
        # Waiting enabling Proceed button
        self.driver.implicitly_wait(10)
        # clicking the Proceed
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="পরবর্তী"]').click()
        # Wainting to load the main screen
        self.driver.implicitly_wait(30)

    def check_balance(self):
        # Click on the check balance
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="ব্যালেন্স দেখুন"]').click()
        self.driver.implicitly_wait(10)
        
    def close_app(self):
        if self.driver:
            self.driver.quit()
            



if __name__ == "__main__":
    bkash_test = BkashAppAutomation()
    bkash_test.start_app()
    bkash_test.enter_app("99805")
    bkash_test.check_balance()
    bkash_test.close_app()