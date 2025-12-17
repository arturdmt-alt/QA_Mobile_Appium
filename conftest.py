import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope='function')
def driver():
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.device_name = 'emulator-5554'
    options.automation_name = 'UiAutomator2'
    
    driver = webdriver.Remote('http://localhost:4723', options=options)
    yield driver
    driver.quit()
