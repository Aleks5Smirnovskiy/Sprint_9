import allure

from data.test_data import build_recipe_data


@allure.feature("Создание рецепта")
class TestRecipeCreation:
    @allure.title("Авторизованный пользователь может создать рецепт")
    def test_authorized_user_can_create_recipe(self, create_recipe_page):
        recipe_data = build_recipe_data()

        recipe_details_page = create_recipe_page.create_recipe(recipe_data)
        recipes_page = recipe_details_page.open_recipes_page()

        assert recipe_details_page.is_recipe_title_displayed(recipe_data.title)
        assert recipes_page.is_recipe_card_displayed(recipe_data.title)
