from selenium.webdriver.common.by import By


class CreateRecipePageLocators:
    PAGE_HEADING = (By.XPATH, "//h1[normalize-space()='Создание рецепта']")
    TITLE_FIELD = (By.XPATH, "//div[.//*[normalize-space()='Название рецепта']]//input")
    INGREDIENT_QUERY_FIELD = (By.XPATH, "//div[.//*[normalize-space()='Ингредиенты']]//input[1]")
    INGREDIENT_AMOUNT_FIELD = (By.XPATH, "//div[.//*[normalize-space()='Ингредиенты']]//input[2]")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//*[normalize-space()='Добавить ингредиент']")
    COOKING_TIME_FIELD = (By.XPATH, "//div[.//*[normalize-space()='Время приготовления']]//input")
    DESCRIPTION_FIELD = (
        By.XPATH,
        "//div[.//*[normalize-space()='Описание рецепта']]//*[self::textarea or self::input]",
    )
    PHOTO_FIELD = (By.CSS_SELECTOR, "input[type='file']")
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Создать рецепт']")

    @staticmethod
    def tag_button(tag_name: str) -> tuple[str, str]:
        return By.XPATH, f"//*[contains(@class,'tag') or self::li or self::span or self::div][normalize-space()='{tag_name}']"

    @staticmethod
    def ingredient_option(ingredient_name: str) -> tuple[str, str]:
        return By.XPATH, f"//div[normalize-space()='{ingredient_name}']"
