import pytest
import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


@pytest.fixture(scope="function")
def driver(request):
    chrome_options = Options()

    # Mobile emulation (Pixel 5)
    mobile_emulation = {
        "deviceMetrics": {"width": 393, "height": 851, "pixelRatio": 2.75},
        "userAgent": (
            "Mozilla/5.0 (Linux; Android 11; Pixel 5) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Mobile Safari/537.36"
        )
    }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    # Headless para CI/CD
    if os.getenv("CI"):
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 🔥 CLAVE PARA HEADLESS + MOBILE
    driver.set_window_size(1200, 1000)
    driver.implicitly_wait(10)

    yield driver

    # Screenshot automático si falla
    if request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot(f"screenshots/{request.node.name}.png")

    driver.quit()


# Hook para detectar fallos
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

