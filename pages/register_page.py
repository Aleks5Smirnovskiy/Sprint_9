from __future__ import annotations

import allure

from data.test_data import UserData
from locators.register_page_locators import RegisterPageLocators
from pages.base_page import BasePage


class RegisterPage(BasePage):
    PAGE_PATH = "/signup"

    def wait_until_opened(self) -> None:
        self.wait_for_url_contains(self.PAGE_PATH)
        self.wait_for_visible(RegisterPageLocators.PAGE_HEADING)

    @allure.step("Register a new user")
    def register(self, user: UserData):
        from pages.login_page import LoginPage

        self.wait_until_opened()
        self.fill(RegisterPageLocators.FIRST_NAME_FIELD, user.first_name)
        self.fill(RegisterPageLocators.LAST_NAME_FIELD, user.last_name)
        self.fill(RegisterPageLocators.USERNAME_FIELD, user.username)
        self.fill(RegisterPageLocators.EMAIL_FIELD, user.email)
        self.fill(RegisterPageLocators.PASSWORD_FIELD, user.password)
        self.wait_for_clickable(RegisterPageLocators.SUBMIT_BUTTON)
        self.click(RegisterPageLocators.SUBMIT_BUTTON)
        login_page = LoginPage(self.driver, self.base_url)
        login_page.wait_for_url_contains(LoginPage.PAGE_PATH)
        return login_page
