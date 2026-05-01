# Sprint_9

UI-автотесты для учебного сервиса Foodgram.

Что входит в проект:
- Page Object с отдельным пакетом локаторов
- Selenium + pytest + Allure
- подготовка тестовых данных через API-фикстуры
- запуск в Docker Compose с Selenoid
- CI workflow для GitHub Actions

Локальный запуск:

```bash
pytest --alluredir=allure-results
allure generate allure-results --clean -o allure-report
```

Запуск в Docker Compose:

```bash
docker compose up --build --abort-on-container-exit --exit-code-from tests
```

