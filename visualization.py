import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt
import os

def plot_skill_distribution(category_count):
    categories = []
    values = []

    for category, count in category_count.items():
        if count > 0:
            categories.append(category.replace("_", " ").title())
            values.append(count)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    axes[0].bar(categories, values)
    axes[0].set_title("Skill Category Distribution (Bar)")
    axes[0].set_xlabel("Category")
    axes[0].set_ylabel("Skill Count")
    axes[0].tick_params(axis='x', rotation=30)

    axes[1].pie(values, labels=categories, autopct="%1.1f%%", startangle=140)
    axes[1].set_title("Skill Distribution by Category (Pie)")

    plt.tight_layout()
    os.makedirs("static/charts", exist_ok=True)
    plt.savefig("static/charts/skill_distribution.png")
    plt.close()
