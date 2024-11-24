import nltk
from nltk.chat.util import reflections

# Download necessary NLTK packages (only required the first time)
nltk.download('punkt')
nltk.download('wordnet')

# Define a list of common greetings the user might use
greetings = ["hi", "hello", "hey", "what's up?"]

# Define a dictionary of FAQs with questions and answers
faq_list = {
    "What is your purpose?": "I am a simple FAQ chatbot designed to answer your questions about [Topic Name].",
    "Can you [action]?": "Unfortunately, I cannot perform actions in the real world yet. I can answer your questions about [Topic Name].",
    "How does [Topic Name] work?": "[Detailed explanation of how the topic works]",
    "What are the benefits of [Topic Name]?": "[List of benefits]",
    "What are the limitations of [Topic Name]?": "[List of limitations]"
}

# Define a function to preprocess user input
def preprocess(text):
    return text.lower()

# Define a function to find the most similar question in the FAQ list
def find_best_match(user_input):
    user_input = preprocess(user_input)
    scores = {faq: nltk.edit_distance(user_input, preprocess(faq)) for faq in faq_list.keys()}
    best_match = min(scores, key=scores.get)
    return best_match, scores[best_match]

# Define a function to respond to the user
def respond(user_input):
    if user_input.lower() in greetings:
        return "Hi! How can I help you today?"
    else:
        best_match, score = find_best_match(user_input)
        if score > 10:  # Arbitrary threshold for a "good" match
            return "Sorry, I don't understand your question. Can you rephrase it?"
        return faq_list.get(best_match, "Sorry, I don't understand your question. Can you rephrase it?")

# Start the chatbot interaction
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye!")
        break
    print("Chatbot: " + respond(user_input))
