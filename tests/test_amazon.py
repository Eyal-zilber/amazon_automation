import pytest

from data.test_data import SEARCH_TERMS
from logger import logger
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
@pytest.mark.parametrize(
    "search_term",
    SEARCH_TERMS
)
def test_amazon_search_and_open_product(
        driver,
        search_term
):

    logger.info(
        f"Starting Amazon test with search term: {search_term}"
    )

    home_page = HomePage(driver)
    search_page = SearchPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Open Amazon
    home_page.open()

    # Search for a product
    home_page.search_product(search_term)
    home_page.click_search()

    # Verify that search results exist
    results_count = search_page.get_results_count()

    print("SEARCH TERM:", search_term)
    print("RESULTS COUNT:", results_count)

    assert results_count > 0

    logger.info(
        "Search results validation passed"
    )

    # Open the first product
    search_page.click_first_product()

    # Get product title
    product_title = product_page.get_product_title()

    print("PRODUCT TITLE:", product_title)

    assert product_title != ""

    logger.info(
        "Product title validation passed"
    )

    # Get product price
    product_price = product_page.get_product_price()

    print("PRODUCT PRICE:", product_price)

    assert product_price != ""

    logger.info(
        "Product price validation passed"
    )

    # Add product to cart
    product_page.add_to_cart()

    # Open cart
    cart_page.open_cart()

    # Get number of items in cart
    cart_items_count = (
        cart_page.get_cart_items_count()
    )

    print(
        "CART ITEMS COUNT:",
        cart_items_count
    )

    assert cart_items_count > 0

    logger.info(
        "Cart validation passed"
    )

    # Proceed to checkout
    checkout_page.proceed_to_checkout()

    # Verify that Amazon moved to the login page
    checkout_page.wait_for_url(
        "/ap/signin"
    )

    print(
        "CHECKOUT REDIRECTED TO LOGIN"
    )

    assert "/ap/signin" in (
        checkout_page.get_current_url()
    )

    logger.info(
        "Checkout redirect validation passed"
    )

    logger.info(
        f"Amazon test completed successfully: {search_term}"
    )