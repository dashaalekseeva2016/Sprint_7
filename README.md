# Sprint_7

Проект по тестированию API учебного сервиса Яндекс Самокат

Описание
Автоматизированные тесты для API сервиса "Яндекс Самокат".

Технологии
- Python 3.14
- pytest
- requests
- allure-pytest

Установка и запуск

1. Клонировать репозиторий:
git clone https://github.com/your-username/Sprint_7.git
cd Sprint_7
Создать виртуальное окружение:
python -m venv venv
source venv/bin/activate  # для macOS/Linux
# или
venv\Scripts\activate  # для Windows
Установить зависимости:
pip install -r requirements.txt
Запустить тесты:
pytest tests/ -v
Запустить с Allure отчетом:
pytest tests/ --alluredir=allure_results
allure serve allure_results
Структура проекта

tests/ - директория с тестами
api_methods/ - методы для работы с API
conftest.py - фикстуры pytest
data.py - тестовые данные
url.py - URL endpoints
requirements.txt - зависимости проекта
Тестируемые endpoints

Создание курьера
Логин курьера
Создание заказа
Получение списка заказов
Принятие заказа
Получение заказа по номеру
Удаление курьера
