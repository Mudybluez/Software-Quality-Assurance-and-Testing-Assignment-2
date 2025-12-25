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
        driver.get(LOGIN_URL)
        username_input = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))
        )
        password_input = driver.find_element(By.CSS_SELECTOR, "#password")
        username_input.clear()
        username_input.send_keys(DEMO_USERNAME)

        password_input.clear()
        password_input.send_keys(DEMO_PASSWORD)

        login_button = driver.find_element(
            By.XPATH, "//button[@type='submit']"
        )
        login_button.click()

        success_message = wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )

        assert "You logged into a secure area!" in success_message.text

        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        driver.save_screenshot(
            os.path.join(SCREENSHOTS_DIR, "login_success.png")
        )

        logout_button = driver.find_element(
            By.XPATH, "//a[contains(@href, 'logout')]"
        )
        logout_button.click()

        logout_message = wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )

        assert "You logged out of the secure area!" in logout_message.text

        driver.save_screenshot(
            os.path.join(SCREENSHOTS_DIR, "logout_success.png")
        )

        print("[OK] Login and logout completed successfully")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_login_logout()
