def generate_recommendations(category_count, role_profile):
    suggestions = []

    for category, expected_weight in role_profile.items():
        if expected_weight > 0 and category_count.get(category, 0) == 0:
            suggestions.append(f"Improve your {category.replace('_', ' ')} skills")

    if not suggestions:
        suggestions.append("Your profile is well balanced for this role")

    return suggestions
