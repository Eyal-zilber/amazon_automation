from selenium.webdriver.common.by import By

from logger import logger
from pages.base_page import BasePage


class ProductPage(BasePage):

    PRODUCT_TITLE = (
        By.ID,
        "productTitle"
    )

    PRODUCT_PRICE = (
        By.ID,
        "apex-pricetopay-accessibility-label"
    )

    ADD_TO_CART_BUTTON = (
        By.ID,
        "add-to-cart-button"
    )

    def get_product_title(self):
        product_title = self.get_text(
            self.PRODUCT_TITLE
        )

        logger.info(
            f"Product title: {product_title}"
        )

        return product_title

    def get_product_price(self):
        product_price = self.get_text_content(
            self.PRODUCT_PRICE
        )

        logger.info(
            f"Product price: {product_price}"
        )

        return product_price

    def add_to_cart(self):
        logger.info("Adding product to cart")

        self.click(
            self.ADD_TO_CART_BUTTON
        )