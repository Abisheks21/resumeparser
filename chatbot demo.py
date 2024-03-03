import nltk
from nltk.chat.util import Chat, reflections

# Define the patterns for greetings and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, thank you!', 'I am doing well, how about you?']),
    (r'(.*) your name?', ["I'm a chatbot AI.", "I am a chatbot, you can call me ChatGPT."]),
    (r'what (.*) want\?', ['I am here to assist you.', 'I am designed to help with various queries.']),
    (r'bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!'])
]

# Create a chatbot using the patterns
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Welcome! How can I assist you today?")
while True:
    user_input = input("> ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    else:
        response = chatbot.respond(user_input)
        print(response)

