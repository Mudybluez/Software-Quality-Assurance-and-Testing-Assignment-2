import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import create_driver
from utils.config import EXPLICIT_WAIT, SCREENSHOTS_DIR


BOOKING_URL = "https://www.blazedemo.com/"


@pytest.mark.booking
def test_flight_booking_flow():
    driver = create_driver()
    wait = WebDriverWait(driver, EXPLICIT_WAIT)

    try:
        driver.get(BOOKING_URL)

        # 1️⃣ Select departure and destination
        from_city = Select(wait.until(
            EC.element_to_be_clickable((By.NAME, "fromPort"))
        ))
        from_city.select_by_visible_text("Paris")

        to_city = Select(wait.until(
            EC.element_to_be_clickable((By.NAME, "toPort"))
        ))
        to_city.select_by_visible_text("Rome")

        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        # 2️⃣ Choose first available flight
        wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )

        driver.find_element(By.CSS_SELECTOR, "table tbody tr td input").click()

        # 3️⃣ Fill passenger form
        wait.until(
            EC.visibility_of_element_located((By.ID, "inputName"))
        )

        driver.find_element(By.ID, "inputName").send_keys("Test User")
        driver.find_element(By.ID, "address").send_keys("Test Address 123")
        driver.find_element(By.ID, "city").send_keys("Astana")
        driver.find_element(By.ID, "state").send_keys("Test State")
        driver.find_element(By.ID, "zipCode").send_keys("010000")

        Select(driver.find_element(By.ID, "cardType")).select_by_visible_text("Visa")

        driver.find_element(By.ID, "creditCardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "creditCardMonth").clear()
        driver.find_element(By.ID, "creditCardMonth").send_keys("12")
        driver.find_element(By.ID, "creditCardYear").clear()
        driver.find_element(By.ID, "creditCardYear").send_keys("2030")
        driver.find_element(By.ID, "nameOnCard").send_keys("TEST USER")

        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        # 4️⃣ Confirmation
        confirmation = wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )

        assert "Thank you for your purchase" in confirmation.text

        # 5️⃣ Screenshot
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        driver.save_screenshot(
            os.path.join(SCREENSHOTS_DIR, "booking_confirmation.png")
        )

    finally:
        driver.quit()
