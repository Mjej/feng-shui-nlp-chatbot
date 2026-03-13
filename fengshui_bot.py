class FengShuiChatbot:
    def __init__(self):
        self.knowledge_base = self.load_knowledge_base()
        self.intents = self.load_intents()

    def load_knowledge_base(self):
        # Load Feng Shui knowledge base
        return {
            "living_room": "The living room is the heart of the home, reflecting harmony and balance.",
            "bedroom": "Your bedroom should promote restful sleep and intimacy, incorporating soft colors and natural materials.",
            "kitchen": "The kitchen is associated with abundance and health. Keeping it clean and organized is essential."
        }

    def load_intents(self):
        # Load intents for various queries related to Feng Shui
        return {
            "greetings": ["hello", "hi", "hey"],
            "goodbye": ["bye", "goodbye", "see you later"],
            "ask_fengshui": ["what does feng shui say about living room?", "how to design my bedroom according to feng shui?"]
        }

    def recognize_intent(self, message):
        for intent, patterns in self.intents.items():
            for pattern in patterns:
                if pattern in message.lower():
                    return intent
        return "unknown"

    def generate_response(self, intent):
        if intent == "greetings":
            return "Hello! How can I assist you with Feng Shui today?"
        elif intent == "goodbye":
            return "Goodbye! Wishing you harmony and balance in your home!"
        elif intent == "ask_fengshui":
            return self.knowledge_base["living_room"]  # Example response
        else:
            return "I'm not sure how to help with that."

    def chat(self, message):
        intent = self.recognize_intent(message)
        response = self.generate_response(intent)
        return response
