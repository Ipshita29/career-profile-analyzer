# Career Profile Analyzer

A Python-based web application that analyzes a user’s skills, projects, and experience to suggest suitable career roles, compute an ATS-style score, and provide actionable recommendations.  
The project is built using a Flask backend with a clean HTML/CSS frontend and visualizes skill distribution using Matplotlib.

---

## 🚀 Features

- Accepts user input for:
  - Skills (comma-separated)
  - Projects with tech stack
  - Years of experience
- Maps skills to predefined categories (Frontend, Backend, Data, AI/ML, etc.)
- Suggests the most suitable career role based on skill distribution
- Calculates an ATS-style score and selection chance
- Generates role match scores for multiple roles
- Provides recommendations for missing or weak skill areas
- Displays a skill summary table
- Visualizes skill distribution using bar and pie charts

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS (Flask templates)  
- **Data Handling:** Python data structures, Pandas  
- **Visualization:** Matplotlib  

---

## 🧠 Project Design Decisions

- This project is intentionally **not labeled as AI/ML** since it does not involve model training, prediction, or evaluation.
- All logic is implemented using **rule-based analysis and scoring**, making the system transparent and easy to explain.
- HTML and CSS are used instead of frontend frameworks to keep the project **focused, simple, and beginner-friendly**.
- Core logic is reusable across both **CLI and web interfaces**.

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install flask pandas matplotlib
```

### 2️⃣ Run the Flask web application

```bash
python app.py
```

Open your browser and visit:

```
http://localhost:5000
```

### 3️⃣ (Optional) Run CLI version

```bash
python main.py
```

---

## 🧪 Example Output

- Suggested Role: Frontend Developer
- ATS Score: 70
- Selection Chance: Medium
- Role match scores for multiple roles
- Personalized skill improvement recommendations
- Skill summary table
- Skill distribution bar and pie charts

---

## 🎯 What This Project Demonstrates

- Backend development using Flask
- Clean separation of logic and presentation
- Rule-based data analysis in Python
- Visualization with Matplotlib
- Building a complete end-to-end application
- Making clear technical choices without overengineering
