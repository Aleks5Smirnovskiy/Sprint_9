from __future__ import annotations

from pathlib import Path

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, base_url: str, timeout: int = 15) -> None:
        self.driver = driver
        self.base_url = base_url.rstrip("/")
        self.wait = WebDriverWait(driver, timeout)

    def build_url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    @allure.step("Open page {path}")
    def open(self, path: str) -> None:
        self.driver.get(self.build_url(path))

    def wait_for_visible(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_presence(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_enabled(self, locator: tuple[str, str]) -> WebElement:
        """Wait for element to become enabled (not disabled)"""
        element = self.wait_for_visible(locator)
        self.wait.until(lambda driver: not element.get_attribute("disabled"))
        return element

    def wait_for_url_contains(self, url_fragment: str) -> bool:
        return self.wait.until(EC.url_contains(url_fragment))

    @allure.step("Click element")
    def click(self, locator: tuple[str, str]) -> None:
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Fill field with value")
    def fill(self, locator: tuple[str, str], value: str) -> None:
        element = self.wait_for_visible(locator)
        element.click()
        element.clear()
        element.send_keys(value)

    @allure.step("Upload file {file_path}")
    def upload_file(self, locator: tuple[str, str], file_path: Path) -> None:
        absolute_path = Path(file_path).resolve()
        self.wait_for_presence(locator).send_keys(str(absolute_path))

    def is_visible(self, locator: tuple[str, str]) -> bool:
        try:
            self.wait_for_visible(locator)
        except Exception:
            return False
        return True
