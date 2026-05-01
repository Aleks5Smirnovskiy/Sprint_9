from selenium.webdriver.common.by import By


class RegisterPageLocators:
    PAGE_HEADING = (By.XPATH, "//h1[normalize-space()='Регистрация']")
    FIRST_NAME_FIELD = (By.NAME, "first_name")
    LAST_NAME_FIELD = (By.NAME, "last_name")
    USERNAME_FIELD = (By.NAME, "username")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Создать аккаунт']")
