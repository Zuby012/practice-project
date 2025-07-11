import re

# Simple knowledge base: question keywords mapped to responses
knowledge_base = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm a bot, but I'm doing great!",
    "bye": "Goodbye! Have a nice day!",
    "name": "I'm a simple chatbot created in Python.",
    "help": "You can ask me about my name, say hello, or say bye."
}


def remove_punctuation(text: str) -> str:
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return cleaned


def get_response(user_input: str) -> str:
    cleaned_input = remove_punctuation(user_input.lower())
    for key in knowledge_base:
        if key in cleaned_input:
            return knowledge_base[key]
    return "Sorry, I don't understand."


print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: " + knowledge_base["bye"])
        break
    response = get_response(user_input)
    print("Chatbot:", response)
