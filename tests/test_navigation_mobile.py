import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Logging global
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


class TestNavigationMobile:

    @pytest.mark.parametrize(
        "language_id, expected_domain",
        [
            ("js-link-box-es", "es.wikipedia"),
            ("js-link-box-en", "en.wikipedia"),
            ("js-link-box-fr", "fr.wikipedia"),
        ]
    )
    def test_mobile_navigation_by_language(self, driver, language_id, expected_domain):
        logging.info(f"Starting mobile navigation test for {expected_domain}")
        
        try:
            driver.get("https://www.wikipedia.org")
            logging.info("Navigated to Wikipedia homepage")
            
            wait = WebDriverWait(driver, 15)
            
            # Click en el idioma
            language_link = wait.until(EC.element_to_be_clickable((By.ID, language_id)))
            language_link.click()
            logging.info(f"Clicked language link: {language_id}")
            
            # Verificar URL
            wait.until(EC.url_contains(expected_domain))
            assert expected_domain in driver.current_url
            logging.info(f"Navigated to {expected_domain}")
            
            # Navegación hacia atrás
            driver.back()
            wait.until(EC.url_contains("www.wikipedia.org"))
            logging.info("Back navigation successful")
            
            # Navegación hacia adelante
            driver.forward()
            wait.until(EC.url_contains(expected_domain))
            logging.info("Forward navigation successful")
            
            logging.info(f"Mobile navigation test PASSED for {expected_domain}")
        
        except Exception as e:
            # Captura screenshot en caso de fallo
            driver.save_screenshot(f"error_navigation_{language_id}.png")
            logging.error(f"Test failed for {expected_domain}: {e}")
            raise
        