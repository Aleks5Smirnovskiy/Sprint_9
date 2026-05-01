import allure

from data.test_data import build_recipe_data


@allure.feature("Создание рецепта")
class TestRecipeCreation:
    @allure.title("Авторизованный пользователь может создать рецепт")
    def test_authorized_user_can_create_recipe(self, create_recipe_page):
        recipe_data = build_recipe_data()

        recipe_details_page = create_recipe_page.create_recipe(recipe_data)
        
        # Проверяем, что находимся на странице деталей рецепта
        current_url = recipe_details_page.driver.current_url
        assert "/recipes/" in current_url
        assert current_url != "https://foodgram-frontend-1.foodgram.education-services.ru/recipes"
