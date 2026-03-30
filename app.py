from flask import Flask, render_template, request
from input_parser import parse_input
from skill_mapper import map_skills_to_categories
from role_inference import infer_best_role
from ats_scorer import calculate_ats_score
from recommendations import generate_recommendations
from role_profiles import ROLE_PROFILES
from visualization import plot_skill_distribution
import pandas as pd
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    analysis = None
    chart_ready = False

    if request.method == "POST":
        skills_input = request.form.get("skills", "").strip()
        projects_input = request.form.get("projects", "").strip()
        experience_input = request.form.get("experience", "0").strip()

        if not skills_input:
            return render_template(
                "index.html",
                analysis=None,
                chart_ready=False,
                error="Please enter your skills to begin analysis."
            )

        # 1️⃣ parse input
        skills, project_skills, experience_years = parse_input(
            skills_input, projects_input, experience_input
        )

        # 2️⃣ map skills
        category_count = map_skills_to_categories(skills, project_skills)

        # 3️⃣ role inference
        best_role, role_scores = infer_best_role(category_count)

        # 4️⃣ ATS score
        ats_score, chance = calculate_ats_score(category_count, experience_years)

        # 5️⃣ recommendations
        recommendations = generate_recommendations(
            category_count,
            ROLE_PROFILES[best_role]
        )

        # 6️⃣ skill summary table (same as CLI)
        df = pd.DataFrame(
            [
                {
                    "Category": k.replace("_", " ").title(),
                    "Skill Count": v
                }
                for k, v in category_count.items()
            ]
        )

        # 7️⃣ plot
        chart_base64 = plot_skill_distribution(category_count)
        chart_ready = chart_base64 is not None

        analysis = {
            "best_role": best_role.replace("_", " ").title(),
            "ats_score": ats_score,
            "chance": chance,
            "role_scores": {
                k.replace("_", " ").title(): v
                for k, v in role_scores.items()
            },
            "recommendations": recommendations,
            "skill_table": df.to_dict(orient="records"),
            "chart_base64": chart_base64
        }

    return render_template(
        "index.html",
        analysis=analysis,
        chart_ready=chart_ready
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port,debug=True)

