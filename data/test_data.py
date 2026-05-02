from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from uuid import uuid4


APP_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = APP_DIR / "assets"
TEST_IMAGE_PATH = ASSETS_DIR / "recipe-image.png"


@dataclass(frozen=True)
class UserData:
    email: str
    username: str
    first_name: str
    last_name: str
    password: str


@dataclass(frozen=True)
class RecipeData:
    title: str
    tag: str
    ingredient_query: str
    ingredient_name: str
    ingredient_amount: str
    cooking_time: str
    description: str
    image_path: Path


def build_user_data() -> UserData:
    unique_suffix = uuid4().hex[:10]
    return UserData(
        email=f"autotest_{unique_suffix}@example.com",
        username=f"autotest_{unique_suffix}",
        first_name="Auto",
        last_name="Tester",
        password="Qwerty12345!",
    )


def build_recipe_data() -> RecipeData:
    unique_suffix = uuid4().hex[:8]
    return RecipeData(
        title=f"Autotest recipe {unique_suffix}",
        tag="Завтрак",
        ingredient_query="сах",
        ingredient_name="сахар",
        ingredient_amount="2",
        cooking_time="5",
        description="Autotest recipe description",
        image_path=TEST_IMAGE_PATH,
    )
