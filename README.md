# Лабораторна робота №3 — Незмінність структур даних у Python

Варіант 7: **Прокат автомобілів**.

Застосовано `@dataclass(frozen=True, slots=True)`, `tuple`, `frozenset`, `MappingProxyType` та `dataclasses.replace`. Чисті операції `add_option`, `extend_rental` і `change_status` створюють нові об'єкти без мутації початкового запису.

## Структура

- `model.py` — незмінні моделі `Rental` і `Car`.
- `core.py` — три чисті функції оновлення.
- `app.py` — демонстраційні дані та консольний вивід.
- `main.py` — точка запуску.
- `tests/test_immutability.py` — перевірки незмінності та коректності.
- `tests/test_benchmark.py` — вимірювання часу pure update та deepcopy-оновлення.
- `report/` — звіт.

## Запуск

```bash
python -m pip install -r requirements.txt
python main.py
python -m pytest -v -s --durations=5
python -m black --check .
python -m ruff check .
python -m mypy model.py core.py app.py main.py
```

Порівняння часу залежить від процесора, версії Python і навантаження. Бенчмарк не стверджує, що незмінний підхід завжди швидший.
