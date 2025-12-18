import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Logging global
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


class TestAmazonMobile:

    def test_amazon_search_mobile(self, driver):
        logging.info("Starting Amazon mobile search test")
        
        try:
            driver.get("https://www.amazon.com")
            logging.info("Navigated to Amazon")
            
            wait = WebDriverWait(driver, 15, poll_frequency=0.5)
            
            # Selector robusto: primero mobile, luego desktop
            search_box = wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "input[name='k'], input#twotabsearchtextbox")
                )
            )
            logging.info("Search box is visible")
            
            search_box.clear()
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
            
        except Exception as e:
            # Captura screenshot si falla
            driver.save_screenshot("error_amazon_mobile.png")
            logging.error(f"Amazon mobile search test FAILED: {e}")
            raise
        
        