from data.skills_db import SKILL_CATEGORY

def get_user_input():

    #skill input
    skill_input = input("Enter your Skills (comma separated): ")
    skill_input = skill_input.lower().strip()
    your_skills= skill_input.split(",")
    your_skills=[skill.strip() for skill in your_skills]
    # print("Skills: ", your_skills)

    #project detail input
    project_input = input("Enter your projects with tech stack (comma separated): ")
    project_input = project_input.lower().strip()
    project_skills = []
    projects = project_input.split("),")  
    for project in projects:
        if "(" in project:
            skills_part = project.split("(")[1].replace(")", "")
            skills = skills_part.split(",")
            for skill in skills:
                skill = skill.strip()
                if skill in SKILL_CATEGORY:
                    project_skills.append(skill)
    # print("Project technologies:", project_skills)


    #experience input 
    experience_input = input("Enter your experience in years (0 if none): ")
    try:
        experience_years = float(experience_input)
    except:
        experience_years = 0.0
    # print ("Experience (in years): ",experience_years)


    # print("Skills: ", your_skills)
    # print("Project technologies:", project_skills)
    # print ("Experience (in years): ",experience_years)
    return your_skills,project_skills,experience_years
