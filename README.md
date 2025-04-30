Selenium Pytest Automation Framework 🚀

A scalable and maintainable test automation framework using Selenium WebDriver, Pytest, and GitHub Actions, built to support CI/CD pipelines, suite-based test execution, and cross-browser support.

📂 Project Structure

HRM_Automation_Framework/
├── config/                # Test suite YAML, environment settings
├── tests/                 # Test cases (smoke, regression, sanity)
├── pages/                 # Page Object Models (POM)
├── utilities/             # BasePage, logger, helpers
├── reports/               # HTML reports (auto-generated)
├── run_suite.py           # CLI runner for test suites
├── conftest.py            # Pytest fixtures (browser/env/screenshot handling)
├── requirements.txt       # Python dependencies
├── pytest.ini             # Marker definitions
├── .gitignore             # Ignore unnecessary files
├── .github/workflows/     # GitHub Actions CI configuration
└── README.md              # This file

✅ Features

🧱 Page Object Model (POM)

🔁 Retry failed tests with pytest-rerunfailures

📸 Capture screenshots on test failure

⚡ Parallel test execution using pytest-xdist

🧪 Marker-based suite filtering (smoke, regression, sanity, etc.)

🛠️ Test suite control via test_suite.yaml

☁️ Integrated with GitHub Actions CI/CD

📄 HTML report generation and upload to GitHub

🚀 How to Run Tests

1. Install dependencies

pip install -r requirements.txt

2. Run test suite via CLI

python run_suite.py smoke --browser=chrome --env=QA

3. View HTML Report

After test run: check reports/ folder

🛠️ GitHub Actions CI

Tests run automatically on:

Every push to main

Every pull request

Artifacts (HTML reports) are uploaded to the Actions → Artifacts section.

🧪 Test Suite Configuration

Defined in: config/test_suite.yaml

suites:
  smoke:
    markers: "smoke"
  regression:
    markers: "regression"
  sanity:
    markers: "sanity"
  critical:
    markers: "critical or sanity"
  full:
    markers: "not skip"

Run any suite:

python run_suite.py regression --browser=edge --env=UAT

📦 Dependencies

selenium
pytest
pytest-html
pytest-xdist
pytest-rerunfailures
pyyaml
webdriver-manager

Install with:
pip install -r requirements.txt