from selenium.webdriver.common.by import By

from logger import logger
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    PROCEED_TO_CHECKOUT_BUTTON = (
        By.ID,
        "sc-buy-box-ptc-button"
    )

    def proceed_to_checkout(self):
        logger.info(
            "Proceeding to checkout"
        )

        self.click(
            self.PROCEED_TO_CHECKOUT_BUTTON
        )

        logger.info(
            "Checkout button clicked"
        )