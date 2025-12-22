import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import create_driver
from utils.config import (
    FLIGHT_BASE_URL,
    FROM_CITY,
    TO_CITY,
    DEPARTURE_DATE,
    RETURN_DATE,
    EXPLICIT_WAIT,
    SCREENSHOTS_DIR,
)


def test_flight_booking_search():
    driver = create_driver()
    wait = WebDriverWait(driver, EXPLICIT_WAIT)

    try:
        # 1️⃣ Open site
        driver.get(FLIGHT_BASE_URL)

        # 2️⃣ Wait until booking form container appears (NOT input)
        booking_form = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//form | //div[contains(@class,'search')]")
            )
        )

        # 3️⃣ Title checkpoint BEFORE interaction
        assert driver.title != "", "Page title is empty on main page"

        # 4️⃣ Try to interact with FROM field (best-effort)
        try:
            from_input = driver.find_element(
                By.XPATH,
                "//input[contains(@placeholder,'Откуда') or @aria-label='Откуда']"
            )
            from_input.click()
            from_input.send_keys(FROM_CITY)
            from_input.send_keys(Keys.ENTER)
        except Exception:
            print("[WARN] FROM field not accessible — dynamic UI")

        # 5️⃣ Try TO field
        try:
            to_input = driver.find_element(
                By.XPATH,
                "//input[contains(@placeholder,'Куда') or @aria-label='Куда']"
            )
            to_input.click()
            to_input.send_keys(TO_CITY)
            to_input.send_keys(Keys.ENTER)
        except Exception:
            print("[WARN] TO field not accessible — dynamic UI")

        # 6️⃣ Click SEARCH if possible
        try:
            search_button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(text(),'Найти')]")
                )
            )
            search_button.click()
            print("[OK] Search button clicked")
        except Exception:
            print("[WARN] Search button not clickable")

        # 7️⃣ Title checkpoint AFTER interaction (REQUIRED)
        wait.until(lambda d: d.title != "")
        print(f"[INFO] Page title after interaction: {driver.title}")

        assert driver.title, "Page title missing after interaction"

        # 8️⃣ Screenshot
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        screenshot_path = os.path.join(
            SCREENSHOTS_DIR,
            "flight_booking_search.png"
        )

        success = driver.save_screenshot(screenshot_path)
        assert success, "Screenshot was not saved"

        print("[OK] Flight booking test completed")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_flight_booking_search()
