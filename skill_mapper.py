from data.skills_db import SKILL_CATEGORY
from input_parser import get_user_input

def map_skills_to_categories():
    skills_list, project_skills, experience_years = get_user_input()
    all_skills = skills_list + project_skills

    category_count = {
        "frontend": 0,
        "backend": 0,
        "data": 0,
        "ai_ml": 0,
        "database": 0,
        "tools": 0
    }

    for skill in all_skills:
        if skill in SKILL_CATEGORY:
            category = SKILL_CATEGORY[skill]
            category_count[category] += 1

    return category_count, experience_years


