import matplotlib.pyplot as plt
import numpy as np


def draw_pythagoras_tree(ax, x, y, angle, length, level):
    """Recursively draws Pythagoras tree branches."""
    if level == 0:
        return

    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    ax.plot([x, x_end], [y, y_end], color="brown", linewidth=max(1, level * 0.5))

    new_length = length * 0.7
    draw_pythagoras_tree(ax, x_end, y_end, angle + np.pi / 4, new_length, level - 1)
    draw_pythagoras_tree(ax, x_end, y_end, angle - np.pi / 4, new_length, level - 1)


def main():
    level = int(input("Enter recursion level (e.g., 10): "))

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect("equal")
    ax.axis("off")

    draw_pythagoras_tree(ax, 0, 0, np.pi / 2, 1, level)

    plt.title(f"Pythagoras Tree (level {level})")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
