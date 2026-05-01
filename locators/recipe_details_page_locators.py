from selenium.webdriver.common.by import By


class RecipeDetailsPageLocators:
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(., 'Добавить в покупки')]")

    @staticmethod
    def recipe_title(title: str) -> tuple[str, str]:
        return By.XPATH, f"//*[self::h1 or self::a][normalize-space()='{title}']"
