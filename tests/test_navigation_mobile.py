import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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

        driver.get("https://www.wikipedia.org")
        wait = WebDriverWait(driver, 30, poll_frequency=0.5)

        # 🧹 CI FIX: ocultar overlays / banners si aparecen
        try:
            overlay = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".overlay-banner, .overlay-banner-control")
                )
            )
            driver.execute_script(
                "arguments[0].style.visibility='hidden';", overlay
            )
            logging.info("Overlay banner hidden")
        except TimeoutException:
            logging.info("No overlay banner detected")

        # 🔍 Esperar link visible (NO clickable para evitar intercept)
        language_link = wait.until(
            EC.presence_of_element_located((By.ID, language_id))
        )

        # 🖱 Click por JS (headless safe)
        driver.execute_script("arguments[0].scrollIntoView(true);", language_link)
        driver.execute_script("arguments[0].click();", language_link)
        logging.info(f"Clicked language link: {language_id}")

        # ✅ Verificación
        wait.until(EC.url_contains(expected_domain))
        assert expected_domain in driver.current_url

        logging.info(f"Navigation successful to {expected_domain}")
