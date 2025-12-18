import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


class TestAmazonMobile:

    def test_amazon_search_mobile(self, driver):
        logging.info("Starting Amazon mobile search test")

        driver.get("https://www.amazon.com")
        logging.info("Navigated to Amazon")

        wait = WebDriverWait(driver, 30, poll_frequency=0.5)

        # 🔥 Selector ultra-robusto
        search_box = wait.until(
            lambda d: d.find_element(
                By.CSS_SELECTOR,
                "input[name='k'], input#twotabsearchtextbox"
            )
        )
        logging.info("Search box located")

        search_box.clear()
        search_box.send_keys("laptop")
        search_box.send_keys(Keys.RETURN)
        logging.info("Search submitted")

        results = wait.until(
            lambda d: d.find_elements(
                By.CSS_SELECTOR,
                '[data-component-type="s-search-result"]'
            )
        )

        logging.info(f"Found {len(results)} results")
        assert len(results) > 0
        logging.info("Amazon mobile search test PASSED")

