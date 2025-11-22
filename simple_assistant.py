import datetime
import webbrowser
import os

class SimpleAssistant:
    def __init__(self):
        self.name = "Assistant"
        
    def get_time(self):
        return datetime.datetime.now().strftime("%H:%M:%S")
    
    def get_date(self):
        return datetime.datetime.now().strftime("%B %d, %Y")
    
    def search_web(self, query):
        webbrowser.open(f"https://google.com/search?q={query}")
        return f"Searching for: {query}"
    
    def calculate(self, expression):
        try:
            result = eval(expression)
            return f"Result: {result}"
        except:
            return "Invalid calculation"
    
    def run(self):
        print(f"Hello! I'm your {self.name}. Type 'help' for commands or 'quit' to exit.")
        
        while True:
            user_input = input("\nYou: ").strip().lower()
            
            if user_input in ['quit', 'exit', 'bye']:
                print("Goodbye!")
                break
            elif user_input == 'help':
                print("Commands: time, date, search [query], calc [expression], open notepad")
            elif user_input == 'time':
                print(f"Current time: {self.get_time()}")
            elif user_input == 'date':
                print(f"Today's date: {self.get_date()}")
            elif user_input.startswith('search '):
                query = user_input[7:]
                print(self.search_web(query))
            elif user_input.startswith('calc '):
                expression = user_input[5:]
                print(self.calculate(expression))
            elif user_input == 'open notepad':
                os.system('notepad')
                print("Opening Notepad...")
            else:
                print("Sorry, I don't understand. Type 'help' for available commands.")

if __name__ == "__main__":
    assistant = SimpleAssistant()
    assistant.run()