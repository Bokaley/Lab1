from pulp import LpVariable, LpProblem, LpMinimize, value
import time

def main():
    print("ЗАДАЧА 1: ОПТИМИЗАЦИЯ РАЦИОНА ПИТАНИЯ (реалистичные цены)")
    
    x1 = LpVariable("Мясо_кг", lowBound=0)
    x2 = LpVariable("Рыба_кг", lowBound=0)
    x3 = LpVariable("Молоко_кг", lowBound=0)
    x4 = LpVariable("Масло_кг", lowBound=0)
    x5 = LpVariable("Сыр_кг", lowBound=0)
    x6 = LpVariable("Крупа_кг", lowBound=0)
    x7 = LpVariable("Картофель_кг", lowBound=0)
    
    # Создание задачи
    problem = LpProblem('Минимальная_стоимость_рациона', LpMinimize)
    
    problem += 450*x1 + 350*x2 + 90*x3 + 180*x4 + 600*x5 + 80*x6 + 40*x7, "Стоимость"
    
    # Ограничения
    problem += 180*x1 + 190*x2 + 30*x3 + 10*x4 + 260*x5 + 130*x6 + 21*x7 >= 118, "Белки"
    problem += 20*x1 + 3*x2 + 40*x3 + 865*x4 + 310*x5 + 30*x6 + 2*x7 >= 56, "Жиры"
    problem += 0*x1 + 0*x2 + 50*x3 + 6*x4 + 20*x5 + 650*x6 + 200*x7 >= 500, "Углеводы"
    problem += 9*x1 + 10*x2 + 7*x3 + 12*x4 + 60*x5 + 20*x6 + 10*x7 >= 8, "Соли"
    
    problem.solve()
    
    # Результаты
    print("\n" + "=" * 70)
    print("ОПТИМАЛЬНЫЙ РАЦИОН С РЕАЛИСТИЧНЫМИ ЦЕНАМИ")
    print("=" * 70)
    
    products = [
        ("Мясо", x1, 450, "руб/кг"),
        ("Рыба", x2, 350, "руб/кг"),
        ("Молоко", x3, 90, "руб/литр"),
        ("Масло", x4, 180, "руб/кг"),
        ("Сыр", x5, 600, "руб/кг"),
        ("Крупа", x6, 80, "руб/кг"),
        ("Картофель", x7, 40, "руб/кг")
    ]
    
    print(f"\n{'ПРОДУКТ':<12} {'КОЛИЧЕСТВО':<15} {'ЦЕНА':<15} {'СТОИМОСТЬ':<15}")
    print("-" * 57)
    
    total_cost = 0
    daily_cost = 0
    monthly_cost = 0
    
    for name, var, price, unit in products:
        quantity = var.varValue
        if quantity > 0.0001:
            cost = quantity * price
            total_cost += cost
            print(f"{name:<12} {quantity:<15.4f} {price:<15} {cost:<15.2f}")
    
    print("-" * 57)
    print(f"{'ВСЕГО:':<12} {'':<15} {'':<15} {total_cost:<15.2f}")
    
    # Расчет на месяц (30 дней)
    daily_cost = total_cost
    monthly_cost = daily_cost * 30
    
    print(f"\nСтоимость питания в день: {daily_cost:.2f} руб.")
    print(f"Стоимость питания в месяц (30 дней): {monthly_cost:.2f} руб.")
    
    # Проверка норм
    print("\n" + "=" * 70)
    print("ПРОВЕРКА ВЫПОЛНЕНИЯ СУТОЧНЫХ НОРМ")
    print("=" * 70)
    
    proteins = 180*x1.varValue + 190*x2.varValue + 30*x3.varValue + 10*x4.varValue + 260*x5.varValue + 130*x6.varValue + 21*x7.varValue
    fats = 20*x1.varValue + 3*x2.varValue + 40*x3.varValue + 865*x4.varValue + 310*x5.varValue + 30*x6.varValue + 2*x7.varValue
    carbs = 0*x1.varValue + 0*x2.varValue + 50*x3.varValue + 6*x4.varValue + 20*x5.varValue + 650*x6.varValue + 200*x7.varValue
    salts = 9*x1.varValue + 10*x2.varValue + 7*x3.varValue + 12*x4.varValue + 60*x5.varValue + 20*x6.varValue + 10*x7.varValue
    
    norms = [
        ("Белки", proteins, 118),
        ("Жиры", fats, 56),
        ("Углеводы", carbs, 500),
        ("Минеральные соли", salts, 8)
    ]
    
    for name, obtained, required in norms:
        percent = (obtained / required) * 100
        status = "ДА" if obtained >= required / 1.000001 else "НЕТ"
        print(f"{name:<20} {obtained:>6.1f} г / {required:>3} г = {percent:>6.1f}% {status}")
    
    # Анализ стоимости питания
    print("\n" + "=" * 70)
    print("АНАЛИЗ СТОИМОСТИ ПИТАНИЯ")
    print("=" * 70)
    
    # Средняя стоимость 100 г белка
    print(f"\nСтоимость 100 г белка из разных продуктов:")
    print(f"• Картофель: {40/21*100:.1f} руб.")
    print(f"• Крупа: {80/130*100:.1f} руб.")
    print(f"• Молоко: {90/30*100:.1f} руб.")
    print(f"• Рыба: {350/190*100:.1f} руб.")
    print(f"• Мясо: {450/180*100:.1f} руб.")
    print(f"• Сыр: {600/260*100:.1f} руб.")

if __name__ == "__main__":
    main()
