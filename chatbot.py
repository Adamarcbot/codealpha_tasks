def get_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi"]:
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I don't understand."

print("Chatbot: Type something (type 'bye' to exit).")

while True:
    user_message = input("You: ")
    reply = get_response(user_message)
    print("Bot:", reply)
    if user_message.lower() == "bye":
        break
