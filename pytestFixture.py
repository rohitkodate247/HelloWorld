# practice pytest

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def browser():
    # Setup: Initialize the WebDriver
    driver = webdriver.Chrome()  # You can use any WebDriver (Chrome, Firefox, etc.)
    driver.get("https://example.com/login")  # Navigate to the login page
    yield driver  # Provide the WebDriver instance to the tests
    # Teardown: Close the browser after tests
    driver.quit()


def test_login_success(browser):
    # Use the WebDriver instance provided by the fixture
    browser.find_element(By.NAME, "username").send_keys("testuser")
    browser.find_element(By.NAME, "password").send_keys("testpassword")
    browser.find_element(By.NAME, "submit").click()

    # Verify successful login (e.g., check for a welcome message)
    assert "Welcome, testuser!" in browser.page_source
