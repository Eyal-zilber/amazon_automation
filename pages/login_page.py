from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    ACCOUNT_LIST = (
        By.ID,
        "nav-link-accountList"
    )

    EMAIL_INPUT = (
        By.ID,
        "ap_email_login"
    )

    CONTINUE_BUTTON = (
        By.ID,
        "continue"
    )

    PASSWORD_INPUT = (
        By.ID,
        "ap_password"
    )

    SIGN_IN_BUTTON = (
        By.ID,
        "signInSubmit"
    )

    def open_login(self):
        self.click(self.ACCOUNT_LIST)

    def enter_email(self, email):
        self.enter_text(self.EMAIL_INPUT, email)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_sign_in(self):
        self.click(self.SIGN_IN_BUTTON)