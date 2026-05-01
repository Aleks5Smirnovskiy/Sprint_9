import allure


@allure.feature("Авторизация")
class TestAuthorization:
    @allure.title("Пользователь может войти в систему")
    def test_user_can_log_in(self, login_page, test_user, attach_screenshot_on_failure):
        registration_page = login_page.go_to_registration_page()
        login_page = registration_page.register(test_user)
        recipes_page = login_page.login(test_user.username, test_user.password)

        assert recipes_page.is_logout_button_displayed()
