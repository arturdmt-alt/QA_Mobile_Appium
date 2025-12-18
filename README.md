# Mobile Web Testing Framework

![Tests](https://img.shields.io/badge/tests-7%20passing%20%7C%201%20skipped-brightgreen)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Selenium](https://img.shields.io/badge/selenium-4.39-orange)
![CI](https://github.com/arturdmt-alt/QA_Mobile_Appium/workflows/Mobile%20Web%20Tests/badge.svg)

Professional mobile web testing framework using Selenium WebDriver with Chrome mobile emulation, CI/CD integration, and production-grade test stability patterns.

## Features

- Mobile web testing with Chrome emulation (Pixel 5: 393x851)
- Parametrized tests using pytest.mark.parametrize
- CI/CD integration with GitHub Actions
- HTML test execution reports
- Robust error handling and stability patterns
- Cross-environment execution (local GUI and CI/CD headless)

## Test Coverage

| Test Suite | Description | Status |
|------------|-------------|--------|
| Google Search | Mobile search functionality | Passing |
| Wikipedia | Article search and navigation | Passing |
| Amazon | Product search validation | Skipped |
| Contact Forms | Form submission and validation | Passing |
| Multi-language Navigation | Parametrized tests (ES, EN, FR) | Passing |

**Total:** 5 test files, 8 test cases (7 passing, 1 skipped)

Note: Amazon test is intentionally skipped due to bot detection. See "Known Challenges" section.

## Tech Stack

- Python 3.11
- Selenium WebDriver 4.39
- pytest 9.0 with parametrize
- webdriver-manager 4.0
- pytest-html 4.1
- Chrome Mobile Emulation (Pixel 5)
- GitHub Actions CI/CD

## Project Structure
```
QA_Mobile_Appium/
├── .github/workflows/
│   └── tests.yml                   # CI/CD pipeline configuration
├── tests/
│   ├── test_web_mobile.py          # Google and Wikipedia tests
│   ├── test_amazon_mobile.py       # Amazon (skipped - bot detection)
│   ├── test_form_mobile.py         # Form submission tests
│   └── test_navigation_mobile.py   # Parametrized multi-language
├── config/
│   └── appium_config.py
├── reports/
│   └── report.html                 # HTML test execution report
├── screenshots/
│   └── *.png                       # Test execution screenshots
├── conftest.py                     # Centralized pytest fixtures
├── pytest.ini                      # Pytest configuration
├── requirements.txt
└── README.md
```

## Installation
```bash
# Clone repository
git clone https://github.com/arturdmt-alt/QA_Mobile_Appium.git
cd QA_Mobile_Appium

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

## Running Tests
```bash
# Run all tests
pytest tests/ -v

# Run with HTML report
pytest tests/ -v --html=reports/report.html --self-contained-html

# Run specific test file
pytest tests/test_web_mobile.py -v

# Run parametrized tests only
pytest tests/test_navigation_mobile.py -v
```

## Key Implementation Details

### Parametrized Testing

The navigation test uses `@pytest.mark.parametrize` to execute multiple test variations:
```python
@pytest.mark.parametrize(
    "language_id, expected_domain",
    [
        ("js-link-box-es", "es.wikipedia"),
        ("js-link-box-en", "en.wikipedia"),
        ("js-link-box-fr", "fr.wikipedia"),
    ]
)
def test_mobile_navigation_by_language(self, driver, language_id, expected_domain):
    # Single test function executes 3 times with different parameters
```

Benefits:
- Follows DRY principles
- Scalable test design
- Data-driven testing approach
- Easy to extend with additional test cases

### Centralized Fixture Management

The `conftest.py` file provides a single fixture for all tests with automatic CI/CD detection:
```python
@pytest.fixture(scope='function')
def driver():
    # Automatically detects CI environment
    if os.getenv("CI"):
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
    # Mobile emulation configuration
```

Advantages:
- No duplicate code across test files
- Automatic environment detection
- Consistent test execution

### CI/CD Integration

GitHub Actions workflow includes:
- Automated test execution on every push
- Chrome browser installation in Linux environment
- Headless browser support for CI
- HTML report artifacts
- Status badge for README

## Known Challenges and Solutions

This section documents real automation challenges encountered and their professional solutions.

### Challenge 1: Amazon Bot Detection

**Problem:**
Amazon actively blocks automated headless browsers using bot detection algorithms, CAPTCHA challenges, and dynamic rendering.

**Impact:**
- Causes unstable test results in CI/CD environments
- Produces false negatives
- Breaks CI pipeline reliability

**Solution:**
The Amazon test is marked with `@pytest.mark.skip`:
```python
@pytest.mark.skip(
    reason="Amazon blocks automated headless browsers with bot detection in CI environments"
)
```

**Rationale:**
- Prevents false negatives in CI pipeline
- Maintains overall test suite stability
- Documents system limitations transparently
- Demonstrates QA decision-making over blind automation

**Alternative approaches considered:**
1. Selenium Stealth plugins - Not maintainable long-term
2. Real device testing with Appium - Outside current project scope
3. API-level testing - Better approach for comprehensive validation

### Challenge 2: Wikipedia Overlay Banners

**Problem:**
In headless CI mode, Wikipedia displays overlay banners that block element clicks, causing `ElementClickInterceptedException`. Tests pass locally but fail in CI.

**Solution:**
Implemented overlay detection and removal before clicking:
```python
try:
    overlay = driver.find_element(By.CSS_SELECTOR, ".overlay-banner")
    driver.execute_script("arguments[0].remove();", overlay)
except:
    pass

# JavaScript-based click as fallback
driver.execute_script("arguments[0].click();", language_link)
```

**Results:**
- Stable navigation tests across all environments
- Zero flaky tests
- Handles real user-facing UI behavior

### Challenge 3: CI vs Local Environment Differences

**Key differences handled:**

| Aspect | Local Environment | CI/CD Environment |
|--------|------------------|-------------------|
| Browser Mode | GUI | Headless |
| Rendering | Full rendering | Optimized rendering |
| Execution Speed | Fast | Variable |
| Overlays/Popups | Rare | Frequent |

**Techniques applied:**
- Explicit waits with WebDriverWait
- Poll frequency tuning for reliability
- JavaScript execution as fallback
- Conditional CI environment detection
- Comprehensive try/except error handling

## Test Results
```
tests/test_web_mobile.py::TestWebMobile::test_google_search_mobile PASSED
tests/test_web_mobile.py::TestWebMobile::test_wikipedia_mobile PASSED
tests/test_amazon_mobile.py::TestAmazonMobile::test_amazon_search_mobile SKIPPED
tests/test_form_mobile.py::TestFormMobile::test_contact_form_mobile PASSED
tests/test_navigation_mobile.py::TestNavigationMobile::test_mobile_navigation_by_language[es] PASSED
tests/test_navigation_mobile.py::TestNavigationMobile::test_mobile_navigation_by_language[en] PASSED
tests/test_navigation_mobile.py::TestNavigationMobile::test_mobile_navigation_by_language[fr] PASSED
```

**Status: 7 passing, 1 skipped (Amazon - bot protection)**

View full HTML report: `reports/report.html`

## CI/CD Pipeline Status

Current status:
- 7 tests passing consistently
- 1 test skipped with documentation
- 0 flaky tests
- Green CI pipeline on every commit

This demonstrates production-ready test automation, not prototype code.

## Author

**Artur Dmytriyev**  
QA Automation Engineer

[LinkedIn](https://www.linkedin.com/in/arturdmytriyev/) 
[GitHub](https://github.com/arturdmt-alt)

## Project Notes

This framework demonstrates professional QA automation practices including:
- Production-grade stability patterns
- Transparent documentation of technical challenges
- Senior-level test design (parametrization, centralized fixtures, CI/CD)
- Real-world problem-solving approach

Designed for QA positions at EA Games, Google, and enterprise companies requiring robust automation frameworks.

## Future Enhancements

Potential improvements for extended project scope:
- Real device testing with Appium
- Playwright comparison and potential migration
- BrowserStack cloud integration for cross-device testing
- Visual regression testing capabilities
- Performance metrics collection
- Allure reporting integration

---

Last updated: December 2025

