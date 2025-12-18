import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import logging


class TestAmazonMobile:

    def test_amazon_search_mobile(self, driver):
        logging.basicConfig(level=logging.INFO)
        logging.info("Starting Amazon mobile search test")
        
        driver.get("https://www.amazon.com")
        logging.info("Navigated to Amazon")
        
        wait = WebDriverWait(driver, 15)
        
        # Search input más estable
        search_box = wait.until(
            EC.visibility_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        logging.info("Search box is visible")
        
        search_box.send_keys("laptop" + Keys.RETURN)
        logging.info("Search submitted")
        
        # Espera resultados
        results = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
            )
        )
        logging.info(f"Found {len(results)} products")
        
        assert len(results) > 0, "No search results found"
        logging.info("Amazon mobile search test PASSED")
        
        