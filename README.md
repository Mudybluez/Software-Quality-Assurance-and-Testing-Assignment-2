# SQAT Assignment 2 — Selenium Automation (Python)

This project contains automated UI tests developed as part of **Software Quality Assurance and Testing (SQAT) – Assignment 2**.

The goal of the assignment is to demonstrate basic skills in:
- UI test automation
- Selenium WebDriver usage
- Test case design
- Working with environment variables
- Handling dynamic web applications

---

## 🛠 Technologies Used

- **Python 3.x**
- **Selenium WebDriver**
- **Chrome WebDriver**
- **dotenv (.env)**
- **Explicit & implicit waits**
- **CSS selectors and XPath**


---

## ⚙️ Environment Variables (`.env`)

All configuration and test data are stored in the `.env` file and loaded via `utils/config.py`.

⚠️ **Important note:**  
The data stored in `.env` is **publicly available demo data** or **non-sensitive test values**.  
No personal, private, or confidential information is used in this project.

🧪 Automated Test Cases
✅ Test Case 1 — Search Functionality (20 pts)
Website: Wikipedia

Verifies search input and navigation to results page

Screenshot saved after search execution

File:

bash
`tests/test_search_info.py`
✅ Test Case 2 — Login / Logout (30 pts)
Website: the-internet.herokuapp.com (demo application)

Uses publicly available demo credentials

Verifies successful login and logout

Screenshots captured for both steps

File:

bash
`tests/test_login_logout.py`
✅ Test Case 3 — Flight Booking Search (40 pts)
Website: tickets.kz

Fills flight search form (From / To / Dates)

Clicks "Search" button

Uses page title checkpoint as required

Screenshot captured after interaction

File:

bash
`tests/test_flight_booking.py`
▶️ How to Run Tests
Activate virtual environment:

bash
`.venv\Scripts\activate`
Run individual tests:

```bash
python -m tests.test_search_info
python -m tests.test_login_logout
python -m tests.test_flight_booking
```
📝 Notes
Real airline websites use CAPTCHA and anti-bot protection.

For this reason, demo applications are used where required (login/logout).

Flight booking test demonstrates interaction and navigation without bypassing security mechanisms.

The project follows best practices for test automation and configuration management.

