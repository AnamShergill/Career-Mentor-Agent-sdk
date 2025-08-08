# agents/job_agent.py

class JobAgent:
    def __init__(self, runner):
        self.runner = runner

    def handle(self, message) -> dict:
        field = message.get("field", "General") if isinstance(message, dict) else message

        roles = [
            {"title": f"{field} Analyst", "desc": "Entry level — data cleaning, visualization, SQL."},
            {"title": f"{field} Engineer", "desc": "Build systems & pipelines."},
            {"title": f"{field} Scientist", "desc": "Research, modeling, experiments."}
        ]
        roles_list = "\n".join([f"- {r['title']}: {r['desc']}" for r in roles])

        return {"text": f"Job roles in {field}:\n{roles_list}\nTip: Showcase projects in your resume."}
