def chatbot():
    while True:
        msg = input("You: ").lower()
        if "hi" in msg:
            print("Bot: Hello!")
        elif "name" in msg:
            print("Bot: I'm ChatBot.")
        elif "bye" in msg:
            print("Bot: Bye!")
            break
        else:
            print("Bot: I don't understand.")
chatbot()
