import random
import re

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            'greeting': ['Hello!', 'Hi there!', 'Hey!', 'Greetings!'],
            'goodbye': ['Goodbye!', 'See you later!', 'Bye!', 'Take care!'],
            'thanks': ['You\'re welcome!', 'No problem!', 'Happy to help!'],
            'name': ['I\'m your AI assistant!', 'You can call me Assistant!'],
            'help': ['I can chat with you, tell jokes, or answer simple questions!'],
            'joke': ['Why did the AI go to therapy? It had too many deep learning issues!',
                    'What do you call a robot that takes the long way around? R2-Detour!'],
            'default': ['That\'s interesting!', 'Tell me more!', 'I see!', 'Hmm, interesting!']
        }
        
        self.patterns = {
            'greeting': r'\b(hi|hello|hey|greetings)\b',
            'goodbye': r'\b(bye|goodbye|see you|farewell)\b',
            'thanks': r'\b(thanks|thank you|thx)\b',
            'name': r'\b(name|who are you|what are you)\b',
            'help': r'\b(help|what can you do)\b',
            'joke': r'\b(joke|funny|humor)\b'
        }
    
    def get_response(self, user_input):
        user_input = user_input.lower()
        
        for intent, pattern in self.patterns.items():
            if re.search(pattern, user_input):
                return random.choice(self.responses[intent])
        
        return random.choice(self.responses['default'])
    
    def chat(self):
        print("Simple Chatbot: Hello! Type 'quit' to exit.")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Chatbot: Goodbye!")
                break
            
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    bot = SimpleChatbot()
    bot.chat()