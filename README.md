Instructions on setup, execution, and understanding the framework:

Project Folder Structure/

python-pytest-api-framework/
│
├── api/
│   └── api_client.py
│
├── tests/
│   └── test_booking_flow.py
│   └── test_negative_cases.py
│
├── conftest.py
├── report.html
└── README.md

1. api/ folder - This is where all API interaction logic lives

api_client.py - Think of this as your universal remote control for APIs. Instead of writing the same code over and over, I created reusable methods (GET, POST, PUT, DELETE) that handle all communication with the server. It manages the base URL and request/response handling, so your tests stay clean and focused.

2. tests/ folder - Your actual test scenarios go here

test_booking_flow.py - The heart of your testing. This covers the complete booking journey: creating a new booking, fetching its details, updating information, and finally deleting it. I've also added data-driven tests here so you can run the same flow with different datasets without duplicating code.

test_negative_cases.py - Testing what shouldn't work is just as important. This file validates error handling: what happens with invalid booking IDs, unauthorized update attempts, and failed deletion scenarios. These tests ensure your API fails gracefully.

3. conftest.py - This is Pytest's configuration file. It handles repetitive setup work like creating the API client and generating authentication tokens before tests run. Instead of writing setup code in every test file, conftest shares these resources automatically across all tests.

4. report.html - Your test execution summary
After running tests, this file gives you a visual, detailed report showing what passed, what failed, and why.

How to Run This Framework:

Step 1: Install Dependencies Open your terminal and run:
This installs pytest (test runner), requests (for API calls), and pytest-html (for generating reports).
└── pip install pytest requests pytest-html

Step 2: Execute All Tests Simply run:
Pytest automatically discovers and executes all test files starting with test_.
└── pytest

Step 3: Generate a Detailed Report Run:
This creates a standalone HTML report with all test results, logs, and failure details.
└── pytest --html=report.html --self-contained-html

Step 4: Open the report in your browser by running
└── start report.html


