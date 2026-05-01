from selenium.webdriver.common.by import By


class LoginPageLocators:
    PAGE_HEADING = (By.XPATH, "//h1[normalize-space()='Войти на сайт']")
    LOGIN_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
    CREATE_ACCOUNT_LINK = (By.XPATH, "//a[@href='/signup' and normalize-space()='Создать аккаунт']")
