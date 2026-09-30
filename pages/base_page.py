from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def enter_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    def get_text_content(self, locator):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
        return element.get_attribute("textContent").strip()

    def is_displayed(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.is_displayed()

    def wait_for_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def clear_field(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()

    def get_attribute(self, locator, attribute):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.get_attribute(attribute)

    def scroll_to_element(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    def get_current_url(self):
        return self.driver.current_url

    def get_page_title(self):
        self.wait.until(
            lambda driver: driver.title != ""
        )
        return self.driver.title

    def press_key(self, locator, key):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.send_keys(key)

    def wait_for_url(self, url):
        self.wait.until(
            EC.url_contains(url)
        )

    def get_elements(self, locator):
        return self.wait.until(
            lambda driver: driver.find_elements(*locator)
        )