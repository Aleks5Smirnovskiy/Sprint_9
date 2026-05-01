from __future__ import annotations

import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from api.client import FoodgramApiClient
from data.test_data import build_user_data
from pages.login_page import LoginPage


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--base-url",
        action="store",
        default=os.getenv("BASE_URL", "https://foodgram-frontend-1.foodgram.education-services.ru"),
    )
    parser.addoption(
        "--api-url",
        action="store",
        default=os.getenv("API_URL", "https://foodgram-backend-1.foodgram.education-services.ru/api"),
    )
    parser.addoption(
        "--selenoid-uri",
        action="store",
        default=os.getenv("SELENOID_URI"),
    )
    parser.addoption(
        "--browser",
        action="store",
        default=os.getenv("BROWSER", "chrome"),
    )
    parser.addoption(
        "--browser-version",
        action="store",
        default=os.getenv("BROWSER_VERSION", "128.0"),
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=os.getenv("HEADLESS", "false").lower() == "true",
    )


@pytest.fixture
def base_url(request: pytest.FixtureRequest) -> str:
    return str(request.config.getoption("--base-url"))


@pytest.fixture
def api_url(request: pytest.FixtureRequest) -> str:
    return str(request.config.getoption("--api-url"))


@pytest.fixture
def browser(request: pytest.FixtureRequest):
    browser_name = str(request.config.getoption("--browser"))
    browser_version = str(request.config.getoption("--browser-version"))
    selenoid_uri = request.config.getoption("--selenoid-uri")
    headless = bool(request.config.getoption("--headless"))

    if browser_name != "chrome":
        raise ValueError("Only chrome browser is configured for this project.")

    options = ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if headless:
        options.add_argument("--headless=new")

    if selenoid_uri:
        options.set_capability("browserName", browser_name)
        options.set_capability("browserVersion", browser_version)
        options.set_capability(
            "selenoid:options",
            {
                "enableVNC": True,
                "enableVideo": False,
            },
        )
        driver = webdriver.Remote(command_executor=selenoid_uri, options=options)
    else:
        driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(autouse=True)
def attach_screenshot_on_failure(request: pytest.FixtureRequest, browser) -> None:
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(
            browser.get_screenshot_as_png(),
            name="failure-screenshot",
            attachment_type=allure.attachment_type.PNG,
        )


@pytest.fixture
def api_client(api_url: str) -> FoodgramApiClient:
    return FoodgramApiClient(api_url)


@pytest.fixture
def test_user():
    return build_user_data()


@pytest.fixture
def login_page(browser, base_url: str) -> LoginPage:
    return LoginPage(browser, base_url).open_page()


@pytest.fixture
def create_recipe_page(login_page, test_user):
    registration_page = login_page.go_to_registration_page()
    login_page = registration_page.register(test_user)
    recipes_page = login_page.login(test_user.username, test_user.password)
    return recipes_page.open_create_recipe_page()
