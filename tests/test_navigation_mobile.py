import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestNavigationMobile:

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

    @pytest.mark.parametrize(
        "language_id, expected_domain",
        [
            ("js-link-box-es", "es.wikipedia"),
            ("js-link-box-en", "en.wikipedia"),
            ("js-link-box-fr", "fr.wikipedia"),
        ]
    )
    def test_mobile_navigation_by_language(
        self, driver, language_id, expected_domain
    ):
        print(f"\n[INFO] Starting mobile navigation test for {expected_domain}")

        driver.get("https://www.wikipedia.org")
        print("[INFO] Navigated to Wikipedia homepage")

        wait = WebDriverWait(driver, 15)

        language_link = wait.until(
            EC.element_to_be_clickable((By.ID, language_id))
        )
        language_link.click()
        print(f"[INFO] Clicked language link: {language_id}")

        wait.until(EC.url_contains(expected_domain))
        assert expected_domain in driver.current_url
        print(f"[INFO] Navigated to {expected_domain}")

        # Back navigation
        driver.back()
        wait.until(EC.url_contains("www.wikipedia.org"))
        print("[INFO] Back navigation successful")

        # Forward navigation
        driver.forward()
        wait.until(EC.url_contains(expected_domain))
        print("[INFO] Forward navigation successful")

        print(f"[INFO] Mobile navigation test PASSED for {expected_domain}")

