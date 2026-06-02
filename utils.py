import json

def save_chat(user_input, bot_response):
    try:
        with open("chat_history.json", "a") as file:
            json.dump({
                "user": user_input,
                "bot": bot_response
            }, file)
            file.write("\n")
    except Exception as e:
        print("Error saving chat:", e)