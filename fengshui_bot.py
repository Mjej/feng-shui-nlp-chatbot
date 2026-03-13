# NLP chatbot
import random

responses = ["Welcome! How can I assist you today?", "Hello! Feel free to ask me anything about Feng Shui.", "Hi there! Let’s chat about Feng Shui!"]

def nlp_chatbot(user_input):
    return random.choice(responses)
