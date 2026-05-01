"""Абсолютно минимальный тест без зависимостей"""


def test_minimal():
    """Проверка что pytest вообще работает"""
    print("=== MINIMAL TEST: Starting ===")
    assert 1 + 1 == 2
    print("=== MINIMAL TEST: Passed ===")
