import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

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
        logging.info(f"Starting navigation test: {expected_domain}")

        driver.get("https://www.wikipedia.org")
        wait = WebDriverWait(driver, 25)

        lang = wait.until(
            lambda d: d.find_element(By.ID, language_id)
        )

        # Click JS (más estable en CI)
        driver.execute_script("arguments[0].click();", lang)
        logging.info(f"Clicked language: {language_id}")

        wait.until(lambda d: expected_domain in d.current_url)
        assert expected_domain in driver.current_url
        logging.info(f"Navigation to {expected_domain} successful")
