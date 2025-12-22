import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import create_driver
from utils.config import (
    LOGIN_URL,
    DEMO_USERNAME,
    DEMO_PASSWORD,
    SCREENSHOTS_DIR,
    EXPLICIT_WAIT
)


def test_login_logout():
    driver = create_driver()
    wait = WebDriverWait(driver, EXPLICIT_WAIT)

    try:
        # 1️⃣ Open login page
        driver.get(LOGIN_URL)

        # 2️⃣ Locate fields (CSS selectors)
        username_input = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))
        )
        password_input = driver.find_element(By.CSS_SELECTOR, "#password")

        # 3️⃣ Enter credentials
        username_input.clear()
        username_input.send_keys(DEMO_USERNAME)

        password_input.clear()
        password_input.send_keys(DEMO_PASSWORD)

        # 4️⃣ Click Login (XPath)
        login_button = driver.find_element(
            By.XPATH, "//button[@type='submit']"
        )
        login_button.click()

        # 5️⃣ Verify successful login
        success_message = wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )

        assert "You logged into a secure area!" in success_message.text

        # Screenshot after login
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        driver.save_screenshot(
            os.path.join(SCREENSHOTS_DIR, "login_success.png")
        )

        # 6️⃣ Logout
        logout_button = driver.find_element(
            By.XPATH, "//a[contains(@href, 'logout')]"
        )
        logout_button.click()

        # 7️⃣ Verify logout
        logout_message = wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )

        assert "You logged out of the secure area!" in logout_message.text

        # Screenshot after logout
        driver.save_screenshot(
            os.path.join(SCREENSHOTS_DIR, "logout_success.png")
        )

        print("[OK] Login and logout completed successfully")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_login_logout()
