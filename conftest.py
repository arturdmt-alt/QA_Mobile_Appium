import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function')
def driver():
    chrome_options = Options()

    # -------------------------------
    # Mobile Emulation
    # -------------------------------
    mobile_emulation = {
        "deviceMetrics": {"width": 393, "height": 851, "pixelRatio": 2.75},
        "userAgent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36"
    }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    # -------------------------------
    # CI/CD / Headless seguro
    # -------------------------------
    if os.getenv("CI"):
        chrome_options.add_argument("--headless")  # más estable que --headless=new
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")  # opcional, mejora compatibilidad

    # Logging para depuración
    chrome_options.add_argument("--enable-logging")
    chrome_options.add_argument("--v=1")

    # -------------------------------
    # Inicialización del driver
    # -------------------------------
    service = Service(
        ChromeDriverManager().install(),
        log_path="chromedriver.log"  # guarda logs de inicio de Chrome
    )
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)

    # -------------------------------
    # Teardown seguro
    # -------------------------------
    try:
        yield driver
    finally:
        driver.quit()

