import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import create_driver
from utils.config import SCREENSHOTS_DIR, EXPLICIT_WAIT


SEARCH_BASE_URL = "https://www.wikipedia.org"
SEARCH_QUERY = "Aviation"


def test_search_information():
    driver = create_driver()
    wait = WebDriverWait(driver, EXPLICIT_WAIT)

    try:
        driver.get(SEARCH_BASE_URL)

        # 1️⃣ Search input (CSS selector)
        search_input = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input#searchInput")
            )
        )

        search_input.clear()
        search_input.send_keys(SEARCH_QUERY)
        search_input.send_keys(Keys.ENTER)

        # 2️⃣ Result page loaded:
        # wait for ANY main content container (language-independent)
        wait.until(
            EC.presence_of_element_located(
                (By.ID, "content")
            )
        )

        # 3️⃣ Assertion: URL changed (search executed)
        assert "wiki" in driver.current_url.lower(), "Search did not navigate to results page"

        # 4️⃣ Screenshot
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        screenshot_path = os.path.join(
            SCREENSHOTS_DIR,
            "search_information.png"
        )

        success = driver.save_screenshot(screenshot_path)

        print("[OK] Wikipedia search page loaded")
        print(f"[OK] Current URL: {driver.current_url}")
        print(f"[OK] Screenshot saved: {success}")

        assert success, "Screenshot was not saved"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_search_information()
