import speech_recognition as sr
import pyttsx3
import openai
import datetime
import webbrowser
import os

class AIAssistant:
    def __init__(self, openai_key=None):
        self.recognizer = sr.Recognizer()
        self.tts = pyttsx3.init()
        self.tts.setProperty('rate', 150)
        if openai_key:
            openai.api_key = openai_key
    
    def speak(self, text):
        print(f"Assistant: {text}")
        self.tts.say(text)
        self.tts.runAndWait()
    
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source, timeout=5)
            try:
                text = self.recognizer.recognize_google(audio)
                print(f"You: {text}")
                return text.lower()
            except:
                return ""
    
    def get_ai_response(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150
            )
            return response.choices[0].message.content
        except:
            return "I need an OpenAI API key to provide AI responses."
    
    def handle_command(self, command):
        if "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            self.speak(f"The time is {time}")
        
        elif "date" in command:
            date = datetime.datetime.now().strftime("%B %d, %Y")
            self.speak(f"Today is {date}")
        
        elif "search" in command:
            query = command.replace("search", "").strip()
            webbrowser.open(f"https://google.com/search?q={query}")
            self.speak(f"Searching for {query}")
        
        elif "open" in command and "notepad" in command:
            os.system("notepad")
            self.speak("Opening notepad")
        
        elif "quit" in command or "exit" in command:
            self.speak("Goodbye!")
            return False
        
        else:
            response = self.get_ai_response(command)
            self.speak(response)
        
        return True
    
    def run(self):
        self.speak("AI Assistant activated. How can I help you?")
        
        while True:
            command = self.listen()
            if command:
                if not self.handle_command(command):
                    break

if __name__ == "__main__":
    # Initialize assistant (add your OpenAI API key for AI responses)
    assistant = AIAssistant()  # AIAssistant("your-openai-key")
    assistant.run()