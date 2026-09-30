from selenium.webdriver.common.by import By

from logger import logger
from pages.base_page import BasePage


class HomePage(BasePage):

    SEARCH_BOX = (
        By.ID,
        "twotabsearchtextbox"
    )

    SEARCH_BUTTON = (
        By.ID,
        "nav-search-submit-button"
    )

    def open(self):
        logger.info("Opening Amazon website")

        self.open_url("https://www.amazon.com")

    def search_product(self, product_name):
        logger.info(
            f"Searching for product: {product_name}"
        )

        self.enter_text(
            self.SEARCH_BOX,
            product_name
        )

    def click_search(self):
        logger.info("Clicking search button")

        self.click(self.SEARCH_BUTTON)