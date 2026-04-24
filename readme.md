# Пример проекта на Flask

Установка библиотек:
```sh
pip install -r requirements.txt
```

Запуск проекта в отладочном режиме:
```sh
flask run --debug
```

Запуск проекта в рабочем (production) режиме:
```sh
gunicorn --bind '0.0.0.0:5000' 'app:create_app()'
```

Запуск модульных тестов:
```sh
pytest
```

Запуск линтера:
```sh
flake8
mymy
```
