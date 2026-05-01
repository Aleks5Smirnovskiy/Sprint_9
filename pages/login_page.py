from __future__ import annotations

import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from pages.recipes_page import RecipesPage
from pages.register_page import RegisterPage


class LoginPage(BasePage):
    PAGE_PATH = "/signin"

    def open_page(self) -> "LoginPage":
        self.open(self.PAGE_PATH)
        self.wait_for_visible(LoginPageLocators.PAGE_HEADING)
        return self

    @allure.step("Open registration page")
    def go_to_registration_page(self) -> RegisterPage:
        self.click(LoginPageLocators.CREATE_ACCOUNT_LINK)
        return RegisterPage(self.driver, self.base_url)

    @allure.step("Log in as existing user")
    def login(self, username: str, password: str) -> RecipesPage:
        self.fill(LoginPageLocators.LOGIN_FIELD, username)
        self.fill(LoginPageLocators.PASSWORD_FIELD, password)
        self.wait_for_clickable(LoginPageLocators.LOGIN_BUTTON)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        recipes_page = RecipesPage(self.driver, self.base_url)
        recipes_page.wait_until_opened()
        return recipes_page

    def is_opened(self) -> bool:
        return self.wait_for_url_contains(self.PAGE_PATH) and self.is_visible(LoginPageLocators.PAGE_HEADING)

    def is_login_form_displayed(self) -> bool:
        return all(
            (
                self.is_visible(LoginPageLocators.LOGIN_FIELD),
                self.is_visible(LoginPageLocators.PASSWORD_FIELD),
                self.is_visible(LoginPageLocators.LOGIN_BUTTON),
            )
        )
