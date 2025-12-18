import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function')
def driver():
    chrome_options = Options()
    
    # Mobile emulation
    mobile_emulation = {
        "deviceMetrics": {
            "width": 393,
            "height": 851,
            "pixelRatio": 2.75
        },
        "userAgent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36"
    }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    
    # CI/CD mode
    if os.getenv('CI'):
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()
    
    