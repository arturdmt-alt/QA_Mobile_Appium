# Mobile Web Testing Framework

![Tests](https://img.shields.io/badge/tests-5%20passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Selenium](https://img.shields.io/badge/selenium-4.39-orange)

Automated mobile web testing framework using **Selenium WebDriver** with Chrome mobile emulation (Pixel 5).

---

## Features

* Mobile web testing with Chrome emulation
* Parametrized tests for scalability
* HTML test reporting
* Multiple test scenarios
* Data-driven testing approach

---

## Test Coverage

* **Google Search** - Mobile search functionality
* **Wikipedia** - Article search and navigation
* **Amazon** - Product search and results validation
* **Contact Forms** - Form submission and validation
* **Multi-language Navigation** - Parametrized language testing (ES, EN, FR)

**Total:** 5 test files | **8 test cases** (including parametrized)

---

## Tech Stack

* Python 3.11
* Selenium WebDriver 4.39
* pytest 9.0 (with parametrize)
* webdriver-manager
* pytest-html
* Chrome Mobile Emulation (Pixel 5 - 393x851)

---

## Project Structure
```
QA_Mobile_Appium/
├── tests/
│   ├── test_web_mobile.py          # Google & Wikipedia tests
│   ├── test_amazon_mobile.py       # Amazon product search
│   ├── test_form_mobile.py         # Form submission
│   └── test_navigation_mobile.py   # Parametrized multi-language
├── config/
│   └── appium_config.py
├── reports/
│   └── report.html
├── venv/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Installation
```bash
# Clone repository
git clone https://github.com/arturdmt-alt/QA_Mobile_Appium.git
cd QA_Mobile_Appium

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## Running Tests
```bash
# Run all tests
pytest tests/ -v

# Run with HTML report
pytest tests/ -v --html=reports/report.html --self-contained-html

# Run specific test file
pytest tests/test_navigation_mobile.py -v -s

# Run parametrized test (executes 3 language variants)
pytest tests/test_navigation_mobile.py::TestNavigationMobile::test_mobile_navigation_by_language -v
```

---

## Key Highlights

### Parametrized Testing
The navigation test uses `@pytest.mark.parametrize` to test multiple languages with a single test function:
- Spanish (es.wikipedia)
- English (en.wikipedia)  
- French (fr.wikipedia)

This demonstrates:
 DRY principles (Don't Repeat Yourself)  
 Scalable test design  
 Data-driven testing approach  
 Professional QA automation practices

---

## Test Results
```
tests/test_web_mobile.py::TestWebMobile::test_google_search_mobile PASSED
tests/test_web_mobile.py::TestWebMobile::test_wikipedia_mobile PASSED
tests/test_amazon_mobile.py::TestAmazonMobile::test_amazon_search_mobile PASSED
tests/test_form_mobile.py::TestFormMobile::test_contact_form_mobile PASSED
tests/test_navigation_mobile.py::TestNavigationMobile::test_mobile_navigation_by_language[es] PASSED
tests/test_navigation_mobile.py::TestNavigationMobile::test_mobile_navigation_by_language[en] PASSED
tests/test_navigation_mobile.py::TestNavigationMobile::test_mobile_navigation_by_language[fr] PASSED
```

**8/8 tests passing**

View full HTML report: `reports/report.html`

---

## Author

**Artur Dmytriyev**  
QA Automation Engineer

[LinkedIn](https://www.linkedin.com/in/arturdmytriyev/) 
[GitHub](https://github.com/arturdmt-alt)

---

## Notes

This framework focuses on mobile web testing best practices including parametrization, clean architecture, and scalability. Demonstrates professional QA automation skills.
