# Django Log Analyzer

CLI-приложение для анализа логов Django-приложений и формирования отчетов.

## 📌 Особенности

- Анализ логов Django (записи `django.requests`)
- Поддержка обработки нескольких файлов одновременно
- Параллельная обработка больших файлов
- Формирование отчетов в консоли
- Расширяемая архитектура для добавления новых отчетов

## 📊 Поддерживаемые отчеты

### `handlers` - Отчет по ручкам API
Группирует запросы по:
- Ручкам API
- Уровням логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)

Пример вывода:
Total requests: 1000

HANDLER DEBUG INFO WARNING ERROR CRITICAL
/admin/dashboard/ 20 72 19 14 18
/api/v1/auth/login/ 23 78 14 15 18
/api/v1/orders/ 26 77 12 19 22
/api/v1/payments/ 26 69 14 18 15
/api/v1/products/ 23 70 11 18 18
/api/v1/shipping/ 60 128 26 32 25
178 494 96 116 116

## 🚀 Установка и запуск

1. Клонируйте репозиторий:
    \`\`\`bash
    git clone https://github.com/yourusername/django-log-analyzer.git

    cd django-log-analyzer
    \`\`\`
2. Установите зависимости:

   \`\`\`bash
   python -m venv .venv
   source .venv/bin/activate
   # Для Linux/Mac
   # или .venv\Scripts\activate для Windows
   pip install pytest pytest-cov
3. Запустите анализатор:

   \`\`\`bash
   python main.py path/to/logs/*.log --report handlers

## 🧪 Тестирование
1. Запуск тестов:

   \`\`\`bash
   pytest -v
   \`\`\`

2. Проверка покрытия:

   \`\`\`bash
   pytest --cov=log_parser --cov-report=term-missing
### 🛠 Как добавить новый отчет
1. Создайте новый класс отчета в log_parser/reports/

2. Реализуйте методы обработки и вывода

3. Добавьте отчет в фабрику (log_parser/factory.py)

4. Напишите тесты

### Пример:

      \`\`\`
    # log_parser/reports/new_report.py
      from .report_base import BaseReport

    class NewReport(BaseReport):
       def process(self, file_paths: list[str]) -> dict:
          # Логика обработки
              pass
        
       def print(self) -> None:
              # Форматированный вывод
              pass

# 📄 Лицензия
MIT


### Инструкция по публикации на GitHub:

1. Создайте новый репозиторий на GitHub:
   - Залогиньтесь на GitHub
   - Нажмите "+" в правом верхнем углу → "New repository"
   - Введите имя (например, `django-log-analyzer`)
   - Выберите "Public"
   - Нажмите "Create repository"

2. Загрузите код в репозиторий:
\`\`\`bash
# Инициализируйте локальный git-репозиторий (если еще не сделано)
git init

# Добавьте все файлы
git add .

# Сделайте коммит
git commit -m "Initial commit"

# Добавьте удаленный репозиторий
git remote add origin https://github.com/yourusername/django-log-analyzer.git

# Запушите изменения
git push -u origin master
\`\`\`
