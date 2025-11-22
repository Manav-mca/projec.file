import json
from datetime import datetime

class AI2025:
    def __init__(self):
        self.knowledge = {}
        self.created = datetime.now().year
    
    def learn(self, topic, data):
        self.knowledge[topic] = data
        return f"Learned: {topic}"
    
    def think(self, query):
        for topic, data in self.knowledge.items():
            if topic.lower() in query.lower():
                return f"Based on {topic}: {data}"
        return "I need to learn more about this topic."
    
    def status(self):
        return {
            "year": self.created,
            "topics_learned": len(self.knowledge),
            "capabilities": ["learn", "think", "adapt"]
        }

# Usage
ai = AI2025()
ai.learn("python", "Modern programming language")
ai.learn("machine_learning", "AI subset for pattern recognition")

print(ai.think("What is python?"))
print(json.dumps(ai.status(), indent=2))