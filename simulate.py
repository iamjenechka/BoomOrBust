import random

def simulate_business():
    capital = 100000  # стартовый капитал
    monthly_expenses = random.randint(5000, 15000)  # случайные расходы
    monthly_income = random.randint(3000, 20000)  # случайный доход
    months = 0

    while capital > 0 and months < 24:  # 2 года работы
        capital += monthly_income - monthly_expenses
        months += 1

    return months >= 24  # Если продержался 2 года – успех

# Запускаем 10 000 симуляций
success_count = sum(simulate_business() for _ in range(10000))

print(f"Вероятность успеха: {success_count / 10000:.2%}")
