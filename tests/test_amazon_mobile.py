import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestAmazonMobile:

    @pytest.fixture(scope="function")
    def driver(self):
        chrome_options = Options()

        mobile_emulation = {
            "deviceMetrics": {
                "width": 393,
                "height": 851,
                "pixelRatio": 2.75
            },
            "userAgent": (
                "Mozilla/5.0 (Linux; Android 11; Pixel 5) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Mobile Safari/537.36"
            )
        }

        chrome_options.add_experimental_option(
            "mobileEmulation", mobile_emulation
        )

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        yield driver
        driver.quit()

    def test_amazon_search_mobile(self, driver):
        print("\n[INFO] Starting Amazon mobile search test")

        driver.get("https://www.amazon.com")
        print("[INFO] Navigated to Amazon")

        wait = WebDriverWait(driver, 15)

        # Mobile search input (Amazon mobile uses name='k')
        search_box = wait.until(
            EC.visibility_of_element_located((By.NAME, "k"))
        )
        print("[INFO] Search box is visible")

        search_box.send_keys("laptop")
        search_box.submit()
        print("[INFO] Search submitted")

        # Wait for search results
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
            )
        )
        print("[INFO] Search results loaded")

        results = driver.find_elements(
            By.CSS_SELECTOR,
            '[data-component-type="s-search-result"]'
        )

        assert len(results) > 0, "No search results found"

        print(f"[INFO] Found {len(results)} products")
        print("[INFO] Amazon mobile search test PASSED")

