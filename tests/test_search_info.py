import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import create_driver
from utils.config import EXPLICIT_WAIT, SCREENSHOTS_DIR


GOOGLE_URL = "https://www.google.com"


@pytest.mark.search
def test_google_search_from_terminal():
    query = input("\n🔎 Enter Google search query: ").strip()
    assert query, "Search query must not be empty"

    driver = create_driver()
    wait = WebDriverWait(driver, EXPLICIT_WAIT)

    try:
        driver.get(GOOGLE_URL)

        # 1️⃣ Accept cookies if present
        try:
            agree_button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[.//text()[contains(., 'Accept') or contains(., 'I agree')]]")
                )
            )
            agree_button.click()
            print("[INFO] Google cookies accepted")
        except Exception:
            print("[INFO] No cookie popup")

        # 2️⃣ Search input
        search_input = wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "q")
            )
        )

        search_input.clear()
        search_input.send_keys(query)
        search_input.send_keys(Keys.ENTER)

        # 3️⃣ Results loaded
        wait.until(
            EC.presence_of_element_located(
                (By.ID, "search")
            )
        )

        # 4️⃣ Screenshot
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        screenshot_path = os.path.join(
            SCREENSHOTS_DIR,
            f"google_search_{query}.png"
        )
        driver.save_screenshot(screenshot_path)

        assert query.lower() in driver.current_url.lower()

        print(f"[OK] Google search completed for: {query}")

    finally:
        driver.quit()
