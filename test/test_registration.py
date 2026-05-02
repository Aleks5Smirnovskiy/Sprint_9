import allure

from data.test_data import build_user_data


@allure.feature("Создание аккаунта")
class TestRegistration:
    @allure.title("Пользователь может создать аккаунт")
    def test_user_can_create_account(self, login_page, attach_screenshot_on_failure):
        user_data = build_user_data()

        registration_page = login_page.go_to_registration_page()
        login_page = registration_page.register(user_data)

        assert login_page.is_opened()
        assert login_page.is_login_form_displayed()
