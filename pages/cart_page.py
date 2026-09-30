from selenium.webdriver.common.by import By

from logger import logger
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_BUTTON = (
        By.ID,
        "nav-cart"
    )

    CART_ITEMS = (
        By.CSS_SELECTOR,
        "div.sc-list-item"
    )

    def open_cart(self):
        logger.info("Opening cart")

        self.click(self.CART_BUTTON)

    def get_cart_items(self):
        items = self.get_elements(
            self.CART_ITEMS
        )

        logger.info(
            f"Cart items found: {len(items)}"
        )

        return items

    def get_cart_items_count(self):
        count = len(
            self.get_cart_items()
        )

        logger.info(
            f"Cart items count: {count}"
        )

        return count

    def is_cart_not_empty(self):
        cart_not_empty = (
            self.get_cart_items_count() > 0
        )

        logger.info(
            f"Cart not empty: {cart_not_empty}"
        )

        return cart_not_empty