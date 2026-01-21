Instructions on setup, execution, and understanding the framework:

Project Folder Structure/

python-pytest-api-framework/
│
├── api/
│ └── api_client.py
│
├── tests/
│ ├── test_booking_flow.py
│ └── test_negative_cases.py
│
├── conftest.py
├── requirements.txt
├── report.html
└── README.md

## Folder and File Description

### api/api_client.py
This file contains reusable API logic.
All HTTP methods like GET, POST, PUT, and DELETE are handled here.
It manages the base URL and request handling so test files stay clean.

### tests/test_booking_flow.py
This file contains the main booking flow tests:
- Create booking
- Get booking
- Update booking
- Delete booking
- Data-driven test using pytest.mark.parametrize

### tests/test_negative_cases.py
This file contains negative test scenarios:
- Fetch non-existing booking
- Update booking without authentication
- Delete booking with invalid booking ID

### conftest.py
This file contains common Pytest fixtures.
It creates the API client and authentication token once and shares them across tests.

### requirements.txt
This file lists project dependencies:
- pytest
- requests
- pytest-html

### report.html
This is the HTML test execution report generated after running tests.

### How to Run This Framework:

### Step 1: Install Dependencies Open your terminal and run:
└── pip install pytest requests pytest-html

### Step 2: Execute All Tests Simply run:
└── pytest

### Step 3: Generate a Detailed Report Run:
└── pytest --html=report.html --self-contained-html

### Step 4: Open the report in your browser by running
└── start report.html


