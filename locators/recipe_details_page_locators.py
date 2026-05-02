from selenium.webdriver.common.by import By


class RecipeDetailsPageLocators:
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(., 'Добавить в покупки')]")
    RECIPE_TITLE = (By.TAG_NAME, "h1")

    @staticmethod
    def recipe_title(title: str) -> tuple[str, str]:
        return By.XPATH, f"//h1[contains(., '{title}')]"
