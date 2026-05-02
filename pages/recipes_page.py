from __future__ import annotations

import allure

from locators.base_page_locators import BasePageLocators
from locators.recipes_page_locators import RecipesPageLocators
from pages.base_page import BasePage


class RecipesPage(BasePage):
    PAGE_PATH = "/recipes"

    def open_page(self) -> "RecipesPage":
        self.open(self.PAGE_PATH)
        self.wait_until_opened()
        return self

    def wait_until_opened(self) -> None:
        self.wait_for_url_contains(self.PAGE_PATH)
        self.wait_for_visible(RecipesPageLocators.PAGE_HEADING)

    @allure.step("Open create recipe page")
    def open_create_recipe_page(self):
        from pages.create_recipe_page import CreateRecipePage

        self.click(RecipesPageLocators.CREATE_RECIPE_LINK)
        create_recipe_page = CreateRecipePage(self.driver, self.base_url)
        create_recipe_page.wait_until_opened()
        return create_recipe_page

    def is_logout_button_displayed(self) -> bool:
        return self.is_visible(BasePageLocators.LOGOUT_BUTTON)

    def is_recipe_card_displayed(self, recipe_title: str) -> bool:
        return self.is_visible(RecipesPageLocators.recipe_title(recipe_title))
