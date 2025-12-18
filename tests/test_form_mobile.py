import pytest
import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configuración de logging global
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


class TestFormMobile:

    def test_contact_form_mobile(self, driver):
        logging.info("Starting mobile contact form test")
        
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        logging.info("Navigated to web form")
        
        wait = WebDriverWait(driver, 15)
        
        try:
            # Text input
            text_input = wait.until(EC.visibility_of_element_located((By.ID, "my-text-id")))
            text_input.send_keys("Mobile Test")
            logging.info("Text input filled")
            
            # Password
            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "my-password")))
            password_input.send_keys("SecurePass123")
            logging.info("Password filled")
            
            # Textarea
            textarea = wait.until(EC.visibility_of_element_located((By.NAME, "my-textarea")))
            textarea.send_keys("This is a test from mobile device")
            logging.info("Textarea filled")
            
            # Submit button
            submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
            submit_button.click()
            logging.info("Form submitted")
            
            # Verificar mensaje de éxito
            success_message = wait.until(EC.visibility_of_element_located((By.ID, "message"))).text
            assert "Received" in success_message, "Form submission failed"
            logging.info("Form submission successful")
            logging.info("Mobile contact form test PASSED")
            
        except Exception as e:
            # Captura screenshot en caso de fallo
            driver.save_screenshot("error_contact_form_mobile.png")
            logging.error(f"Test failed: {e}")
            raise
        