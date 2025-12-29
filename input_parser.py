def parse_input(skill_input, project_input, experience_input):
    # ---- SKILLS ----
    skills = [s.strip().lower() for s in skill_input.split(",") if s.strip()]

    # ---- PROJECTS ----
    project_skills = []
    projects = project_input.lower().split("),")
    for project in projects:
        if "(" in project:
            skills_part = project.split("(")[1].replace(")", "")
            for s in skills_part.split(","):
                s = s.strip()
                if s:
                    project_skills.append(s)

    # ---- EXPERIENCE ----
    try:
        experience = float(experience_input)
    except:
        experience = 0.0

    return skills, project_skills, experience


def get_user_input():
    skill_input = input("Enter your Skills (comma separated): ")
    project_input = input("Enter your projects with tech stack (comma separated): ")
    experience_input = input("Enter your experience in years (0 if none): ")

    return parse_input(skill_input, project_input, experience_input)
