# runner.py
from agents.career_agent import CareerAgent
from agents.skill_agent import SkillAgent
from agents.job_agent import JobAgent

class Runner:
    def __init__(self):
        self.agents = {
            "CareerAgent": CareerAgent(self),
            "SkillAgent": SkillAgent(self),
            "JobAgent": JobAgent(self)
        }
        self.active_agent = "CareerAgent"

    def handle_user_message(self, message: str):
        agent = self.agents[self.active_agent]
        response = agent.handle(message)

        if "handoff_to" in response:
            target = response["handoff_to"]
            if target in self.agents:
                self.active_agent = target
                payload = response.get("payload", "")
                next_res = self.agents[target].handle(payload)
                return f"{response['text']}\n\n{next_res['text']}"

        return response["text"]
