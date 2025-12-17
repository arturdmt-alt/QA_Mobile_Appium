import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebMobile:
    
    @pytest.fixture(scope='function')
    def driver(self):
        """Setup Chrome driver for mobile web testing"""
        chrome_options = Options()
        
        # Mobile emulation con dimensiones manuales
        mobile_emulation = {
            "deviceMetrics": {
                "width": 393,
                "height": 851,
                "pixelRatio": 2.75
            },
            "userAgent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
        }
        
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        
        # Setup driver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(10)
        
        yield driver
        
        driver.quit()
    
    def test_google_search_mobile(self, driver):
        """Test Google search on mobile web"""
        print('\n🚀 Starting mobile web test...')
        
        driver.get('https://www.google.com')
        print('✅ Navigated to Google')
        
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'q'))
        )
        print('✅ Found search box')
        
        search_box.send_keys('Appium mobile testing')
        search_box.submit()
        print('✅ Submitted search')
        
        WebDriverWait(driver, 10).until(
        EC.url_contains('search')
        )
        print('✅ Results loaded')
        
        assert 'Appium' in driver.title or 'Appium' in driver.page_source
        
        print('✅ Mobile web test PASSED!')
    
    def test_wikipedia_mobile(self, driver):
        """Test Wikipedia mobile navigation"""
        print('\n🚀 Starting Wikipedia mobile test...')
        
        driver.get('https://www.wikipedia.org')
        print('✅ Navigated to Wikipedia')
        
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'searchInput'))
        )
        print('✅ Found search input')
        
        search_input.send_keys('Python programming')
        search_input.submit()
        print('✅ Submitted search')
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'content'))
        )
        print('✅ Article loaded')
        
        assert 'Python' in driver.title
        
        print('✅ Wikipedia mobile test PASSED!')
        
        