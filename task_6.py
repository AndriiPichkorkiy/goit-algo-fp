items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

for _, item in items.items():
    item["ration"] = item["calories"] / item["cost"]


def greedy_algorithm(items: dict[str, dict[str, int]], budget: int):
    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["ration"], reverse=True)

    for title, values in sorted_items:
        cost = values["cost"]
        calories = values["calories"]

        if remaining_budget >= cost:
            remaining_budget -= cost
            total_calories += calories
            chosen_items.append(title)
        else:
            break

    return dict({
        "Всього калорій": total_calories,
        "Грошовий залишок": remaining_budget,
        "Страви": chosen_items
    })


def dynamic_programming(items: dict[str, dict[str, int]], budget: int):
    item_names = list(items.keys())
    item_costs = [items[name]["cost"] for name in item_names]
    item_calories = [items[name]["calories"] for name in item_names]
    n = len(items)

    # Таблиця динамічного програмування
    dp_table = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнення таблиці
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if item_costs[i - 1] <= w:
                dp_table[i][w] = max(
                    dp_table[i - 1][w],
                    dp_table[i - 1][w - item_costs[i - 1]] +
                    item_calories[i - 1]
                )
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    chosen_items = []
    remaining_budget = budget
    total_calories = dp_table[n][budget]

    for i in range(n, 0, -1):
        if dp_table[i][remaining_budget] != dp_table[i - 1][remaining_budget]:
            chosen_items.append(item_names[i - 1])
            remaining_budget -= item_costs[i - 1]

    return dict({
        "Всього калорій": total_calories,
        "Грошовий залишок": remaining_budget,
        "Страви": chosen_items[::-1]  # Зворотній порядок для зручності
    })


if __name__ == "__main__":
    budget = 100
    print("Жадібний алгоритм:", greedy_algorithm(items, budget))
    print("Динамічне програмування:", dynamic_programming(items, budget))
