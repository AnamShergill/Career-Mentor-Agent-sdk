# main.py
from runner import Runner

if __name__ == "__main__":
    runner = Runner()
    print("Career Mentor Agent - type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        bot_reply = runner.handle_user_message(user_input)
        print(f"Bot: {bot_reply}\n")
