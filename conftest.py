import os

import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    # Take screenshot if the test failed
    if request.node.rep_call.failed:
        screenshots_dir = "screenshots"

        os.makedirs(screenshots_dir, exist_ok=True)

        screenshot_name = (
            f"{request.node.name}.png"
        )

        screenshot_path = os.path.join(
            screenshots_dir,
            screenshot_name
        )

        driver.save_screenshot(screenshot_path)

        print(
            f"Screenshot saved: {screenshot_path}"
        )

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(
        item,
        f"rep_{report.when}",
        report
    )