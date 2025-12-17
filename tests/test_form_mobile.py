import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestFormMobile:

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

    def test_contact_form_mobile(self, driver):
        print("\n[INFO] Starting mobile contact form test")

        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        print("[INFO] Navigated to web form")

        wait = WebDriverWait(driver, 15)

        text_input = wait.until(
            EC.visibility_of_element_located((By.ID, "my-text-id"))
        )
        text_input.send_keys("Mobile Test")
        print("[INFO] Text input filled")

        password_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "my-password"))
        )
        password_input.send_keys("SecurePass123")
        print("[INFO] Password filled")

        textarea = wait.until(
            EC.visibility_of_element_located((By.NAME, "my-textarea"))
        )
        textarea.send_keys("This is a test from mobile device")
        print("[INFO] Textarea filled")

        submit_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit_button.click()
        print("[INFO] Form submitted")

        success_message = wait.until(
            EC.visibility_of_element_located((By.ID, "message"))
        ).text

        assert "Received" in success_message, "Form submission failed"

        print("[INFO] Form submission successful")
        print("[INFO] Mobile contact form test PASSED")

