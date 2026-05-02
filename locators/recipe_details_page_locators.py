from selenium.webdriver.common.by import By


class RecipeDetailsPageLocators:
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(., 'Добавить в покупки')]")
    RECIPE_TITLE = (By.TAG_NAME, "h1")

    @staticmethod
    def recipe_title(title: str) -> tuple[str, str]:
        # Регистронезависимый поиск названия в h1
        return By.XPATH, f"//h1[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'), '{title.lower()}')]"
