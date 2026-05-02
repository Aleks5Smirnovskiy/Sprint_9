from selenium.webdriver.common.by import By


class RecipesPageLocators:
    PAGE_HEADING = (By.XPATH, "//h1[contains(normalize-space(), 'Рецепты')]")
    CREATE_RECIPE_LINK = (By.XPATH, "//a[@href='/recipes/create']")

    @staticmethod
    def recipe_title(title: str) -> tuple[str, str]:
        return By.XPATH, f"//main//a[normalize-space()='{title}']"
