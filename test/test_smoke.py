import allure


@allure.feature("Smoke test")
class TestSmoke:
    @allure.title("Simple smoke test")
    def test_simple_smoke(self):
        """Минимальный тест для проверки CI/CD"""
        assert True
        
    @allure.title("Browser opens")
    def test_browser_opens(self, browser, attach_screenshot_on_failure):
        """Проверка что браузер открывается"""
        browser.get("https://www.google.com")
        assert "Google" in browser.title
