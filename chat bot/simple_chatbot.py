import re

# Simple knowledge base: question keywords mapped to responses
knowledge_base = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm a bot, but I'm doing great!",
    "bye": "Goodbye! Have a nice day!",
    "name": "I'm a simple chatbot created in Python.",
    "help": "You can ask me about my name, say hello, or say bye."
}

user_correction = "x"  # just a placeholder for the user_correction variable

# function to add new request and response to knowledge_base


def add_new_content(user_input, user_correction):
    user_correction = input(
        "--Would you help by telling me the correct response: ")
    knowledge_base[user_input] = user_correction

# function to filter every punctuation from request before getting response


def remove_punctuation(text: str) -> str:
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return cleaned

# function to get response after removing punctuations


def get_response(user_input: str) -> str:
    cleaned_input = remove_punctuation(user_input.lower())
    for key in knowledge_base:
        if key in cleaned_input:
            return knowledge_base[key]
    print("Sorry i don't understand")
    add_new_content(user_input, user_correction)
    return "Thank you."


print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("--You: ")
    if user_input.lower() == "bye":
        print("Chatbot: " + knowledge_base["bye"])
        break
    response = get_response(user_input)
    print("Chatbot:", response)
