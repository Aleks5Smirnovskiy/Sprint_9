from selenium.webdriver.common.by import By


class BasePageLocators:
    RECIPES_LINK = (By.XPATH, "//a[@href='/recipes']")
    LOGOUT_BUTTON = (By.XPATH, "//*[normalize-space()='Выход']")
