import random

def russian_roulette_simulation(trials=100000):
    total_days = 730  # 2 года
    shots_per_day = 3
    chamber_size = 500  # 500 гнезд, одно смертельное
    death_count = 0
    
    for _ in range(trials):
        alive = True
        for _ in range(total_days * shots_per_day):
            if random.randint(1, chamber_size) == 1:
                death_count += 1
                alive = False
                break
    
    survival_rate = (trials - death_count) / trials
    
    print(f"Выживаемость: {survival_rate * 100:.2f}%")
    print(f"Шанс погибнуть: {(1 - survival_rate) * 100:.2f}%")
    if survival_rate > 0:
        expected_payout = survival_rate * 1_000_000
        print(f"Ожидаемый выигрыш: ${expected_payout:,.2f}")
    else:
        print("Никто не выжил :(")

# Запуск симуляции
russian_roulette_simulation()
