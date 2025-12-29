from skill_mapper import map_skills_to_categories
from role_inference import infer_best_role
from ats_scorer import calculate_ats_score
from recommendations import generate_recommendations
from role_profiles import ROLE_PROFILES
from visualization import plot_skill_distribution
import pandas as pd


def main():
    # -------- SKILL MAPPING --------
    category_count, experience_years = map_skills_to_categories()

    # -------- ROLE INFERENCE --------
    best_role, role_scores = infer_best_role(category_count)

    # -------- ATS SCORE --------
    ats_score, chance = calculate_ats_score(category_count, experience_years)

    print("\n===== ANALYSIS RESULT =====")
    print("Best suited role:", best_role.replace("_", " ").title())
    print("ATS Score:", ats_score)
    print("Selection Chance:", chance)

    # -------- ROLE MATCH SCORES --------
    print("\nRole Match Scores:")
    for role, score in role_scores.items():
        print(role.replace("_", " ").title(), "→", score)

    # -------- RECOMMENDATIONS --------
    print("\nRecommendations:")
    recommendations = generate_recommendations(
        category_count,
        ROLE_PROFILES[best_role]
    )
    for rec in recommendations:
        print("-", rec)

    # -------- PANDAS SKILL SUMMARY (FROM COUNTS) --------
    df = pd.DataFrame(
        [
            {
                "Category": category.replace("_", " ").title(),
                "Skill Count": count
            }
            for category, count in category_count.items()
        ]
    )

    print("\nSkill Summary Table:")
    print(df)

    # -------- VISUALIZATION (LAST – BLOCKING) --------
    plot_skill_distribution(category_count)


if __name__ == "__main__":
    main()
