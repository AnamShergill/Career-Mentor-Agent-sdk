# 🎓 Career Mentor Agent

A Python-based multi-agent system that guides students through career exploration using specialized agents for career suggestions, skill development, and job opportunities.

---

## 🧠 What It Does
The Career Mentor Agent helps users explore career paths through a structured, agent-based approach:
- **Recommends career paths** based on user interests.
- **Generates skill roadmaps** using the `get_career_roadmap()` tool for any chosen field.
- **Provides job role insights** relevant to the selected career.
- **Agent Handoff** – seamlessly switches between:
  - **CareerAgent** – suggests possible fields.
  - **SkillAgent** – shows skill-building plans.
  - **JobAgent** – shares real-world job examples.

---

## ⚙️ Technologies Used
- **Python 3**
- **OpenAI Agent SDK** + Runner
- **Custom Tools**: Skill Roadmap Generator
- **Multi-Agent Handoff Mechanism**

---

## 📂 Project Structure

- career_mentor/
- runner.py # Handles running and switching between agents
- tools.py # Contains custom tool functions (e.g., get_career_roadmap)
- agents/
- init.py # Initializes the agents package
- career_agent.py # Suggests career fields
- skill_agent.py # Generates skill development roadmaps
- job_agent.py # Lists relevant job roles
- main.py # Entry point to run the program




---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/Career-Mentor-Agent.git
cd Career-Mentor-Agent

