from input_parser import get_user_input
from skill_mapper import map_skills_to_categories
from role_inference import infer_best_role
from ats_scorer import calculate_ats_score
from recommendations import generate_recommendations
from role_profiles import ROLE_PROFILES
from visualization import plot_skill_distribution
import pandas as pd

def main():
    skills, project_skills, experience_years = get_user_input()

    category_count = map_skills_to_categories(skills, project_skills)

    best_role, role_scores = infer_best_role(category_count)
    ats_score, chance = calculate_ats_score(category_count, experience_years)

    print("\n===== ANALYSIS RESULT =====")
    print("Best suited role:", best_role.replace("_", " ").title())
    print("ATS Score:", ats_score)
    print("Selection Chance:", chance)

    print("\nRole Match Scores:")
    for role, score in role_scores.items():
        print(role.replace("_", " ").title(), "→", score)

    print("\nRecommendations:")
    recs = generate_recommendations(category_count, ROLE_PROFILES[best_role])
    for r in recs:
        print("-", r)

    df = pd.DataFrame([
        {"Category": k.replace("_", " ").title(), "Skill Count": v}
        for k, v in category_count.items()
    ])
    print("\nSkill Summary Table:")
    print(df)

    plot_skill_distribution(category_count)

if __name__ == "__main__":
    main()
