items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    """Greedy algorithm: selects items by best calories/cost ratio."""
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    selected = []
    total_cost = 0
    total_calories = 0

    for name, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected.append(name)
            total_cost += info["cost"]
            total_calories += info["calories"]

    return selected, total_calories


def dynamic_programming(items, budget):
    """Dynamic programming: finds optimal set for maximum calories."""
    names = list(items.keys())
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    selected = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = names[i - 1]
            selected.append(name)
            w -= items[name]["cost"]

    return selected[::-1], dp[n][budget]


if __name__ == "__main__":
    budget = 100

    print(f"Budget: {budget}\n")

    greedy_result, greedy_calories = greedy_algorithm(items, budget)
    greedy_cost = sum(items[item]["cost"] for item in greedy_result)
    print("Greedy Algorithm:")
    print(f"  Selected: {greedy_result}")
    print(f"  Total cost: {greedy_cost}")
    print(f"  Total calories: {greedy_calories}")

    print()

    dp_result, dp_calories = dynamic_programming(items, budget)
    dp_cost = sum(items[item]["cost"] for item in dp_result)
    print("Dynamic Programming:")
    print(f"  Selected: {dp_result}")
    print(f"  Total cost: {dp_cost}")
    print(f"  Total calories: {dp_calories}")
