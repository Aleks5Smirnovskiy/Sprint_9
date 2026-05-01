from __future__ import annotations

from selenium.webdriver.common.by import By

from locators.recipe_details_page_locators import RecipeDetailsPageLocators
from pages.base_page import BasePage
from pages.recipes_page import RecipesPage


class RecipeDetailsPage(BasePage):
    def wait_until_opened(self, recipe_title: str) -> None:
        self.wait_for_url_contains("/recipes/")
        # Ждем появления любого заголовка h1 на странице
        self.wait_for_visible((By.XPATH, "//h1"))

    def is_recipe_title_displayed(self, recipe_title: str) -> bool:
        return self.is_visible(RecipeDetailsPageLocators.recipe_title(recipe_title))

    def open_recipes_page(self) -> RecipesPage:
        recipes_page = RecipesPage(self.driver, self.base_url)
        recipes_page.open_page()
        return recipes_page
