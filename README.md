# QA Automation Project Study

Учебный проект по автоматизации тестирования веб-приложения с использованием **Selenium**, **Pytest** и подхода **Page Object Model (POM)**.

## 🧰 Технологии

- Python 3.10+
- Selenium WebDriver
- Pytest
- Page Object Model (POM)

## 📁 Структура проекта

```
qa_auto_project_study/
├── pages/                # Page Object классы
├── tests/                # Автоматизированные тесты
├── conftest.py           # Общие фикстуры и настройки
├── requirements.txt      # Список зависимостей
└── README.md             # Описание проекта
```

## 🚀 Запуск проекта

1. Клонируйте репозиторий:

```bash
git clone https://github.com/AntonShishkin11/qa_auto_project_study.git
cd qa_auto_project_study
```

2. Создайте виртуальное окружение и активируйте его:

```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Запустите тесты:

```bash
pytest -v
```

## 📌 Назначение

Проект предназначен для практики написания автотестов и структурирования кода по шаблону Page Object. Используется в учебных целях.
