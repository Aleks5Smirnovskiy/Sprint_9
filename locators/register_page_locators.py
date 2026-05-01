from selenium.webdriver.common.by import By


class RegisterPageLocators:
    PAGE_HEADING = (By.XPATH, "//h1[normalize-space()='Регистрация']")
    FIRST_NAME_FIELD = (By.XPATH, "//div[.//*[normalize-space()='Имя']]//input")
    LAST_NAME_FIELD = (By.XPATH, "//div[.//*[normalize-space()='Фамилия']]//input")
    USERNAME_FIELD = (By.XPATH, "//div[.//*[normalize-space()='Имя пользователя']]//input")
    EMAIL_FIELD = (By.XPATH, "//div[.//*[normalize-space()='Адрес электронной почты']]//input")
    PASSWORD_FIELD = (By.XPATH, "//div[.//*[normalize-space()='Пароль']]//input")
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Создать аккаунт']")
