import random
import matplotlib.pyplot as plt

ANALYTICAL_PROBABILITIES = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
    8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}


def monte_carlo_simulation(num_rolls):
    """Simulates dice rolls and counts sum occurrences."""
    counts = {s: 0 for s in range(2, 13)}

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        counts[dice1 + dice2] += 1

    probabilities = {s: count / num_rolls for s, count in counts.items()}
    return probabilities


def print_comparison_table(monte_carlo_probs):
    """Prints comparison table of Monte Carlo vs analytical results."""
    print(f"{'Sum':<6}{'Monte Carlo':<15}{'Analytical':<15}{'Difference':<12}")
    print("-" * 48)

    for s in range(2, 13):
        mc = monte_carlo_probs[s] * 100
        an = ANALYTICAL_PROBABILITIES[s] * 100
        diff = abs(mc - an)
        print(f"{s:<6}{mc:.2f}%{'':<9}{an:.2f}%{'':<9}{diff:.2f}%")


def plot_comparison(monte_carlo_probs):
    """Plots comparison chart."""
    sums = list(range(2, 13))
    mc_values = [monte_carlo_probs[s] * 100 for s in sums]
    an_values = [ANALYTICAL_PROBABILITIES[s] * 100 for s in sums]

    x = range(len(sums))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    bars1 = ax.bar([i - width/2 for i in x], mc_values, width, label="Monte Carlo", color="steelblue")
    bars2 = ax.bar([i + width/2 for i in x], an_values, width, label="Analytical", color="coral")

    ax.set_xlabel("Sum")
    ax.set_ylabel("Probability (%)")
    ax.set_title("Dice Roll Probabilities: Monte Carlo vs Analytical")
    ax.set_xticks(x)
    ax.set_xticklabels(sums)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    num_rolls = 1000000

    print(f"Monte Carlo simulation with {num_rolls:,} dice rolls\n")

    monte_carlo_probs = monte_carlo_simulation(num_rolls)

    print_comparison_table(monte_carlo_probs)
    print()

    plot_comparison(monte_carlo_probs)
