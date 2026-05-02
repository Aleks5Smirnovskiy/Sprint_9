from __future__ import annotations

from dataclasses import asdict

import requests

from data.test_data import UserData


class FoodgramApiClient:
    def __init__(self, base_api_url: str) -> None:
        self.base_api_url = base_api_url.rstrip("/")
        self.session = requests.Session()

    def create_user(self, user: UserData) -> dict:
        payload = asdict(user)
        response = self.session.post(
            f"{self.base_api_url}/users/",
            json=payload,
            timeout=15,
        )
        response.raise_for_status()
        return response.json()
