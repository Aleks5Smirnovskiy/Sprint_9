import allure
import pytest


@allure.feature("Smoke test")
class TestSmoke:
    @allure.title("Simple smoke test")
    def test_simple_smoke(self):
        """Минимальный тест для проверки CI/CD"""
        print("=== SMOKE TEST: Simple assert starting ===")
        assert True
        print("=== SMOKE TEST: Simple assert passed ===")
        
    @allure.title("Browser opens")
    def test_browser_opens(self, browser, attach_screenshot_on_failure):
        """Проверка что браузер открывается"""
        print("=== SMOKE TEST: Browser test starting ===")
        print(f"=== Browser object: {browser} ===")
        browser.get("https://www.google.com")
        print(f"=== Browser title: {browser.title} ===")
        assert "Google" in browser.title
        print("=== SMOKE TEST: Browser test passed ===")

