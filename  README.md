# Amazon Automation Framework

A professional UI automation framework for testing the Amazon website using Python, Selenium WebDriver, and Pytest.

## Project Overview

This project automates a main Amazon shopping flow:

1. Open Amazon
2. Search for a product
3. Verify search results
4. Open the first product
5. Verify product title
6. Verify product price
7. Add the product to the cart
8. Open the cart
9. Verify that the cart contains the product
10. Proceed to checkout
11. Verify that Amazon redirects to the login page

The test is parametrized and runs with multiple search terms.

## Technologies

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Pytest Parametrization
- Pytest Markers
- Allure Reports
- Python Logging
- Git
- GitHub
- Jenkins
- HTML Test Reports

## Framework Architecture

The project follows the Page Object Model architecture.

```text
amazon_automation/
│
├── conftest.py
├── logger.py
├── main.py
├── pytest.ini
├── requirements.txt
├── README.md
│
├── data/
│   └── test_data.py
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── search_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── login_page.py
│
├── tests/
│   ├── test_amazon.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_login.py
│   ├── test_product.py
│   └── test_search.py
│
└── utils/


Authorgit add

Eyal Zilber

QA Team Leader | Automation | Selenium | Python | DevOps