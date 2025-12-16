# Тесты для FastAPI приложения

Этот каталог содержит комплексные тесты для FastAPI приложения с аутентификацией.

## Структура тестов

```
tests/
├── __init__.py                 # Инициализация пакета тестов
├── conftest.py                # Конфигурация pytest и фикстуры
├── test_main.py               # Тесты основного приложения
├── test_auth.py               # Тесты аутентификации
├── test_schemas.py            # Тесты Pydantic схем
├── test_dao.py                # Тесты DAO классов
├── test_utils.py              # Тесты утилит
├── test_config.py             # Тесты конфигурации
├── test_exceptions.py         # Тесты исключений
├── test_integration.py        # Интеграционные тесты
├── test_performance.py        # Тесты производительности
├── requirements-test.txt      # Зависимости для тестов
└── README.md                  # Этот файл
```

## Типы тестов

### Unit тесты
- `test_schemas.py` - тестирование валидации данных
- `test_utils.py` - тестирование утилит (хеширование паролей, токены)
- `test_config.py` - тестирование конфигурации
- `test_exceptions.py` - тестирование пользовательских исключений

### Integration тесты
- `test_main.py` - тестирование основных эндпоинтов
- `test_auth.py` - тестирование роутеров аутентификации
- `test_dao.py` - тестирование работы с базой данных
- `test_integration.py` - полные сценарии использования

### Performance тесты
- `test_performance.py` - тесты производительности и нагрузки

## Установка зависимостей

```bash
# Установка основных зависимостей
uv sync
# Установка тестовых зависимостей
uv pip install -r tests/requirements-test.txt
```

## Запуск тестов

### Все тесты
```bash
pytest tests/ -v
```

### Только unit тесты
```bash
pytest tests/ -v -m "not integration and not slow"
```

### Только интеграционные тесты
```bash
pytest tests/test_integration.py -v
```

### Тесты с покрытием кода
```bash
pytest tests/ --cov=app --cov-report=term-missing --cov-report=html
```

### Тесты производительности
```bash
pytest tests/test_performance.py -v -m slow
```

### Параллельный запуск тестов
```bash
pytest tests/ -n auto
```

## CI/CD интеграция

Тесты готовы для интеграции с CI/CD системами. Пример для GitHub Actions:

```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.12
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install -r tests/requirements-test.txt
    - name: Run tests
      run: pytest tests/ --cov=app --cov-report=xml
    - name: Upload coverage
      uses: codecov/codecov-action@v1
```
