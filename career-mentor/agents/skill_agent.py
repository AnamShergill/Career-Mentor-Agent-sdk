# agents/skill_agent.py
from tools import get_career_roadmap

class SkillAgent:
    def __init__(self, runner):
        self.runner = runner

    def handle(self, message) -> dict:
        if isinstance(message, dict) and "field" in message:
            field = message["field"]
        else:
            field = message

        roadmap = get_career_roadmap(field) # type: ignore
        milestones = "\n".join([f"Week {m['week']}: {m['goal']}" for m in roadmap["milestones"]])

        return {
            "text": (
                f"Skill Roadmap for {roadmap['field']}:\n"
                f"Summary: {roadmap['summary']}\n"
                f"Timeline: {roadmap['timeline_weeks']} weeks\n"
                f"Milestones:\n{milestones}\n\n"
                "Would you like to see (A) Weekly breakdown, (B) Project ideas, or (C) Handoff to JobAgent?"
            )
        }
