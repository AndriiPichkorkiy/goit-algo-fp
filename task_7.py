from collections import Counter, defaultdict
import random

# розрахунок методом Монте-Карло


# Симуляція методом Монте-Карло
def monte_carlo_simulation(attempts=1_000_000):
    monte_carlo_statistic = defaultdict(int)

    # Симуляція кидків кубиків
    for _ in range(attempts):
        result = random.randint(1, 6) + random.randint(1, 6)
        monte_carlo_statistic[result] += 1

    # Обчислення ймовірностей
    monte_carlo_probabilities = {
        outcome: count / attempts for outcome, count in monte_carlo_statistic.items()}

    print("Таблиця ймовірностей методом Монте-Карло:")
    for outcome, probability in sorted(monte_carlo_probabilities.items()):
        print(
            f"Сума: {outcome}, Ймовірність: {probability:.2%} ({monte_carlo_statistic[outcome]}/{attempts})")

    return monte_carlo_probabilities


# аналітичні розрахунки


def analytical_probabilities():
    outcomes = [i + j for i in range(1, 7) for j in range(1, 7)]
    count_outcomes = Counter(outcomes)

    total_outcomes = 36  # загальна кількість можливих результатів
    probability_table = {
        outcome: count / total_outcomes for outcome, count in count_outcomes.items()}

    print("\nТаблиця аналітичних ймовірностей:")
    for outcome, probability in sorted(probability_table.items()):
        print(
            f"Сума: {outcome}, Ймовірність: {probability:.2%} ({count_outcomes[outcome]}/{total_outcomes})")

    return probability_table


# Порівняння результатів без графіка
def compare_probabilities():
    monte_carlo_probs = monte_carlo_simulation()
    analytical_probs = analytical_probabilities()

    print("{:<10} | {:<20} | {:<20}".format(
        "Сума", "Метод Монте-Карло", "Аналітичний розрахунок"))
    print("-" * 55)
    for sum_ in range(2, 13):
        monte_carlo_value = monte_carlo_probs.get(sum_, 0)
        analytical_value = analytical_probs.get(sum_, 0)
        print("{:<10} | {:<20.4%} | {:<20.4%}".format(
            sum_, monte_carlo_value, analytical_value))


# Виклик функції
if __name__ == "__main__":
    compare_probabilities()
