from __future__ import annotations

import allure

from data.test_data import RecipeData
from locators.create_recipe_page_locators import CreateRecipePageLocators
from pages.base_page import BasePage
from pages.recipe_details_page import RecipeDetailsPage


class CreateRecipePage(BasePage):
    PAGE_PATH = "/recipes/create"

    def wait_until_opened(self) -> None:
        self.wait_for_url_contains(self.PAGE_PATH)
        self.wait_for_visible(CreateRecipePageLocators.PAGE_HEADING)

    @allure.step("Create a new recipe")
    def create_recipe(self, recipe: RecipeData) -> RecipeDetailsPage:
        self.fill(CreateRecipePageLocators.TITLE_FIELD, recipe.title)
        self.click(CreateRecipePageLocators.tag_button(recipe.tag))
        ingredient_field = CreateRecipePageLocators.INGREDIENT_QUERY_FIELD
        self.fill(ingredient_field, recipe.ingredient_query)
        ingredient_locator = CreateRecipePageLocators.ingredient_option(recipe.ingredient_name)
        self.wait_for_visible(ingredient_locator)
        self.click(ingredient_locator)
        self.fill(CreateRecipePageLocators.INGREDIENT_AMOUNT_FIELD, recipe.ingredient_amount)
        self.click(CreateRecipePageLocators.ADD_INGREDIENT_BUTTON)
        self.fill(CreateRecipePageLocators.COOKING_TIME_FIELD, recipe.cooking_time)
        self.fill(CreateRecipePageLocators.DESCRIPTION_FIELD, recipe.description)
        self.upload_file(CreateRecipePageLocators.PHOTO_FIELD, recipe.image_path)
        self.click(CreateRecipePageLocators.SUBMIT_BUTTON)
        recipe_details_page = RecipeDetailsPage(self.driver, self.base_url)
        recipe_details_page.wait_until_opened(recipe.title)
        return recipe_details_page
