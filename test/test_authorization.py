import allure


@allure.feature("Авторизация")
class TestAuthorization:
    @allure.title("Пользователь может войти в систему")
    def test_user_can_log_in(self, login_page, api_user):
        recipes_page = login_page.login(api_user.username, api_user.password)

        assert recipes_page.is_logout_button_displayed()
