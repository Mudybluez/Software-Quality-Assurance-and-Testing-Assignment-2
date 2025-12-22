import os
from dotenv import load_dotenv

# Load .env from project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))


SCREENSHOTS_DIR = os.path.join(
    BASE_DIR,
    os.getenv("SCREENSHOTS_DIR", "screenshots")
)

BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", 5))
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", 15))
PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", 30))

CHROME_DRIVER_PATH = os.path.join(
    BASE_DIR,
    os.getenv("CHROME_DRIVER_PATH")
)
# Demo login (Assignment 2)
LOGIN_URL = os.getenv("LOGIN_URL")
DEMO_USERNAME = os.getenv("DEMO_USERNAME")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")

# Flight booking (Assignment 2)
FLIGHT_BASE_URL = os.getenv("FLIGHT_BASE_URL")
FROM_CITY = os.getenv("FROM_CITY")
TO_CITY = os.getenv("TO_CITY")
DEPARTURE_DATE = os.getenv("DEPARTURE_DATE")
RETURN_DATE = os.getenv("RETURN_DATE")