Лабораторная работа 1: Оптимизация рациона питания
https://img.shields.io/badge/Python-3.8+-blue.svg
https://img.shields.io/badge/PuLP-2.6+-green.svg
https://img.shields.io/badge/License-MIT-yellow.svg
https://colab.research.google.com/assets/colab-badge.svg
 Описание проекта
Решение задачи оптимизации дневного рациона питания с минимальной стоимостью при соблюдении норм потребления питательных веществ. Проект включает реализацию на Python с использованием библиотеки PuLP и решение в Excel/Google Sheets.

Задача: Составить дневной рацион минимальной стоимости, удовлетворяющий нормам потребления:

Белки: ≥ 118 г

Жиры: ≥ 56 г

Углеводы: ≥ 500 г

Минеральные соли: ≥ 8 г

Структура проекта
lab1/
├── report/                    # Отчеты
├── task1.py                  # Решение на Python (PuLP)  
├── task1_opensolver.xlsx     # Решение в Excel/Google Sheets
└── README.md                 # Инструкция  
Установка и запуск
Клонирование репозитория:

bash
git clone https://github.com/yourusername/lab1-diet-optimization.git
cd lab1-diet-optimization
Установка зависимостей:

bash
pip install -r requirements.txt
Запуск решения:

bash
python src/task1_pulp.py
Использование в Google Colab
https://colab.research.google.com/assets/colab-badge.svg

Откройте ноутбук в Google Colab

Установите зависимости: !pip install pulp

Запустите все ячейки
​
 
Результаты
Оптимальный рацион
Продукт	Количество	Цена за кг	Стоимость
Молоко	1.133 кг	90 руб/кг	102.00 руб
Крупа	0.410 кг	80 руб/кг	32.82 руб
Итого	1.543 кг	-	134.82 руб
Выполнение норм питания
Питательное вещество	Получено	Норма	% выполнения
Белки	118.00 г	118 г	100.0%
Жиры	86.93 г	56 г	155.2%
Углеводы	500.00 г	500 г	100.0%
Минеральные соли	11.53 г	8 г	144.2%
Стоимость питания
В день: 134.82 руб

В неделю: 943.74 руб

В месяц (30 дней): 4,044.60 руб

В год: 49,209.30 руб

Технические детали
Используемые библиотеки
PuLP — библиотека для линейного программирования

Методы решения
Симплекс-метод (реализован в PuLP)

Ручной подбор в Excel/Google Sheets

Анализ чувствительности к изменению цен
В Excel
Файл: docs/excel_solution.xlsx

Использованы функции СУММПРОИЗВ()

Настроена проверка данных

Добавлены диаграммы для визуализации

Использование кода
Базовое использование
python
from src.task1_pulp import solve_diet_problem

# Решение задачи
results = solve_diet_problem()

# Получение результатов
print(f"Минимальная стоимость: {results['total_cost']:.2f} руб.")
print(f"Оптимальный рацион: {results['solution']}")
Изменение цен
python
# Создание пользовательских цен
custom_prices = {
    'Мясо': 500,      # руб/кг
    'Рыба': 400,      # руб/кг
    'Молоко': 100,    # руб/литр
    'Масло': 200,     # руб/кг
    'Сыр': 700,       # руб/кг
    'Крупа': 100,     # руб/кг
    'Картофель': 50   # руб/кг
}

# Решение с пользовательскими ценами
from src.task1_pulp import solve_with_custom_prices
results = solve_with_custom_prices(custom_prices)
Анализ чувствительности
python
from src.analysis import analyze_price_sensitivity

# Анализ влияния изменения цен на решение
sensitivity_results = analyze_price_sensitivity(
    base_prices=custom_prices,
    variations=0.1  # ±10%
)

