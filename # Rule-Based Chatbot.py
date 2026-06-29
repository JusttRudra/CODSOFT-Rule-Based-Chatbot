# Rule-Based Chatbot
# CodSoft Internship Project

from datetime import datetime

print("=" * 50)
print("🤖 Welcome to Rule-Based Chatbot")
print("Type 'bye' to exit.")
print("=" * 50)

while True:
    user = input("\nYou: ").lower().strip()

    if user == "bye":
        print("Bot: Goodbye! Have a great day. 😊")
        break

    elif user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you today?")

    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "your name" in user:
        print("Bot: I'm a Rule-Based Chatbot created for the CodSoft Internship.")

    elif "who created you" in user:
        print("Bot: I was created by Rudransh Sharma using Python.")

    elif "who is rudransh sharma" in user or "rudransh sharma" in user:
        print("Bot: Rudransh Sharma is the greatest man ever lived in the history of humankind and also happens to be the developer of this AI chatbot. 😎")

    elif "help" in user:
        print("Bot: I can answer simple questions like greetings, time, date, weather, and more.")

    elif "time" in user:
        current_time = datetime.now().strftime("%I:%M %p")
        print("Bot: The current time is", current_time)

    elif "date" in user:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    elif "weather" in user:
        print("Bot: Sorry, I can't access live weather data.")

    elif "thank" in user:
        print("Bot: You're welcome! 😊")

    elif "python" in user:
        print("Bot: Python is a powerful and beginner-friendly programming language.")

    elif "college" in user:
        print("Bot: That's interesting! Which college are you studying in?")

    elif "age" in user:
        print("Bot: I don't have an age because I'm a computer program.")

    else:
        print("Bot: Sorry, I didn't understand that. Please try another question.")