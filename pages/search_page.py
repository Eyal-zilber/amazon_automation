from selenium.webdriver.common.by import By

from logger import logger
from pages.base_page import BasePage


class SearchPage(BasePage):

    SEARCH_RESULTS = (
        By.CSS_SELECTOR,
        "[data-component-type='s-search-result']"
    )

    PRODUCT_TITLES = (
        By.CSS_SELECTOR,
        "[data-component-type='s-search-result'] h2"
    )

    def get_results_count(self):
        results = self.get_elements(
            self.SEARCH_RESULTS
        )

        results_count = len(results)

        logger.info(
            f"Search results count: {results_count}"
        )

        return results_count

    def get_product_titles(self):
        elements = self.get_elements(
            self.PRODUCT_TITLES
        )

        titles = []

        for element in elements:
            titles.append(element.text)

        logger.info(
            f"Retrieved {len(titles)} product titles"
        )

        return titles

    def click_first_product(self):
        logger.info("Clicking first product")

        elements = self.get_elements(
            self.PRODUCT_TITLES
        )

        elements[0].click()