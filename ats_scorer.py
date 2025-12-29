def calculate_ats_score(category_count, experience_years):
    skill_score = sum(category_count.values()) * 5

    # Experience contribution
    if experience_years == 0:
        experience_score = 0
    elif experience_years <= 1:
        experience_score = 10
    elif experience_years <= 2:
        experience_score = 20
    else:
        experience_score = 30

    ats_score = min(skill_score + experience_score, 100)

    if ats_score >= 75:
        chance = "High"
    elif ats_score >= 50:
        chance = "Medium"
    else:
        chance = "Low"

    return ats_score, chance
