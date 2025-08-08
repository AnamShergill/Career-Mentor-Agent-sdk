# agents/career_agent.py

class CareerAgent:
    def __init__(self, runner):
        self.runner = runner

    def handle(self, message: str) -> dict:
        msg = message.lower()

        if any(word in msg for word in ["help", "career", "interested in"]):
            return {"text": "Tell me your interests or subjects you enjoy (e.g., coding, design, data, healthcare)."}

        guessed_fields = self.guess_fields(message)
        if guessed_fields:
            fields_list = "\n".join(f"{i+1}. {f}" for i, f in enumerate(guessed_fields))
            return {"text": f"Based on your interests, you might like:\n{fields_list}\nReply with a number or field name."}

        if "data science" in msg or msg.strip() == "1":
            return {
                "text": "Great — I’ll pass you to SkillAgent for a Data Science roadmap.",
                "handoff_to": "SkillAgent",
                "payload": {"field": "Data Science"}
            }

        return {"text": "Sorry, I didn't get that. Please share your interests or a field name."}

    def guess_fields(self, message: str):
        mapping = [
            (["code", "coding", "python"], "Software Engineering"),
            (["data", "analysis", "machine learning"], "Data Science"),
            (["design", "ux", "graphics"], "UX Design"),
            (["health", "medicine"], "Healthcare")
        ]
        found = []
        msg = message.lower()
        for keywords, field in mapping:
            if any(k in msg for k in keywords):
                found.append(field)
        return found
