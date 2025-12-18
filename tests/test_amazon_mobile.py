import pytest
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


@pytest.mark.skip(reason="Amazon blocks automated headless browsers with bot detection and CAPTCHA in CI environments")
class TestAmazonMobile:

    def test_amazon_search_mobile(self, driver):
        logging.info("Amazon mobile search test skipped due to bot detection")

