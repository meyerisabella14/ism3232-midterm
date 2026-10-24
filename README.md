# ISM3232 Midterm: Seabreeze Inn

- **Name:** Isabella Meyer
- **Version:** DELTA
- **Date:** October 24, 2026

## What This Program Does

This program calculates reservation totals for Seabreeze Inn. It applies stay discounts and cleaning fees, then determines whether guests need credit checks or receive welcome packages. It prints each reservation and a summary of all eight stays.

## Business Rules

1. Room cost equals the nightly rate multiplied by the number of nights.
2. Stays under four nights receive no standard discount, stays of four through thirteen nights receive 6%, and stays of fourteen or more nights receive 18%.
3. Corporate guests receive at least a 6% discount.
4. A $40 cleaning fee applies when the discounted room cost is $300 or less.
5. A total of $2,000 or more requires a credit check.
6. A welcome package requires more than five nights and a total of at least $1,000.

## How to Run

From the repository folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```

## How to Test

There are 28 tests covering all eight functions, rule boundaries, corporate discounts, ties, empty lists, and report formatting.

```bash
ruff format --check .
ruff check .
pytest -v
```

## Files in This Repository

- `business_rules.py`: Eight functions and the business-rule constants.
- `main.py`: Reservation data, report printing, and summary counts.
- `commands.md`: Terminal commands, actual outputs, and explanations.
- `README.md`: Project description and instructions.
- `requirements.txt`: Python dependencies recorded with pip freeze.
- `.gitignore`: Excludes the virtual environment and generated caches.
- `tests/__init__.py`: Marks the tests folder as a Python package.
- `tests/test_business_rules.py`: The 28 business-rule tests.

## AI Use Statement

I used ChatGPT for step-by-step guidance, code and test generation, and documentation assistance.
