# tools.py

def get_career_roadmap(field: str) -> dict:
    """Returns a mock skill roadmap for a given career field."""
    if field.lower() == "data science":
        return {
            "field": "Data Science",
            "summary": "Learn Python, statistics, machine learning, and deployment.",
            "skills": [
                {"name": "Python for Data", "level": "beginner", "description": "Numpy, pandas, EDA"},
                {"name": "Statistics", "level": "beginner", "description": "Descriptive stats, probability"},
                {"name": "Machine Learning", "level": "intermediate", "description": "Regression, classification, evaluation"},
                {"name": "Deployment", "level": "advanced", "description": "APIs, model monitoring"}
            ],
            "timeline_weeks": 26,
            "milestones": [
                {"week": 4, "goal": "Basic Python and EDA projects"},
                {"week": 12, "goal": "Train and evaluate ML models"},
                {"week": 20, "goal": "End-to-end project + portfolio"}
            ],
            "resources": [
                {"title": "Python for Data Science Course", "type": "course"},
                {"title": "Hands-On Machine Learning Book", "type": "book"}
            ]
        }
    else:
        return {
            "field": field,
            "summary": f"Roadmap for {field} (details not available)",
            "skills": [],
            "timeline_weeks": 12,
            "milestones": [],
            "resources": []
        }
