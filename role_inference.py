import numpy as np
from role_profiles import ROLE_PROFILES

def infer_best_role(category_count):
    categories = list(category_count.keys())
    user_vector = np.array([category_count[cat] for cat in categories])
    if np.sum(user_vector) == 0:
        return None, {}

    user_vector = user_vector / np.sum(user_vector)

    role_scores = {}

    for role, weights in ROLE_PROFILES.items():
        role_vector = np.array([weights.get(cat, 0) for cat in categories])
        distance = np.linalg.norm(user_vector - role_vector)

        similarity = 1 / (1 + distance)
        role_scores[role] = round(similarity, 2)

    best_role = max(role_scores, key=role_scores.get)
    return best_role, role_scores
