import allure

from data.test_data import build_recipe_data


@allure.feature("Создание рецепта")
class TestRecipeCreation:
    @allure.title("Авторизованный пользователь может создать рецепт")
    def test_authorized_user_can_create_recipe(self, create_recipe_page, attach_screenshot_on_failure):
        recipe_data = build_recipe_data()

        recipe_details_page = create_recipe_page.create_recipe(recipe_data)
        
        # Проверяем, что перешли на страницу деталей рецепта
        recipe_details_page.wait_for_url_contains("/recipes/")
        
        # Проверяем, что отображается название рецепта
        assert recipe_details_page.is_recipe_title_displayed(recipe_data.title)
