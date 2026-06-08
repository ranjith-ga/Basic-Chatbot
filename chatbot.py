def chatbot():
    print("🤖 Simple Chatbot Started (type 'exit' or 'bye' to stop)")
    print("Try: hello, how are you, what is your name, what can you do, help, good morning, good night")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi! 👋")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! 😊 How about you?")

        elif user_input == "what is your name":
            print("Bot: I'm your simple Python chatbot 🤖")

        elif user_input == "what can you do":
            print("Bot: I can chat with you using simple rules!")

        elif user_input == "help":
            print("Bot: You can try saying hello, how are you, bye, good morning, etc.")

        elif user_input == "good morning":
            print("Bot: Good morning! ☀️ Have a nice day!")

        elif user_input == "good night":
            print("Bot: Good night! 🌙 Sweet dreams!")

        elif user_input == "who created you":
            print("Bot: I was created using Python programming 🐍")

        elif user_input == "tell me a joke":
            print("Bot: Why do programmers hate nature? Because it has too many bugs! 😂")

        elif user_input == "bye":
            print("Bot: Goodbye! Take care 👋")
            break

        elif user_input == "exit":
            print("Bot: Exiting chatbot... 👋")
            break

        else:
            print("Bot: Sorry 😕 I don't understand that. Try 'help'.")

# Run chatbot
if __name__ == '__main__':
    chatbot()
