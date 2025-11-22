import openai
import asyncio
import time
import numpy as np
import tensorflow as tf
from dataclasses import dataclass
from typing import Dict, List, Callable

class AIChat:
    def __init__(self, api_key: str):
        self.client = openai.OpenAI(api_key=api_key)
        self.conversation = []
    
    def send_message(self, message: str) -> str:
        try:
            self.conversation.append({"role": "user", "content": message})
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.conversation
            )
            
            ai_response = response.choices[0].message.content
            self.conversation.append({"role": "assistant", "content": ai_response})
            return ai_response
        except Exception as e:
            return f"Error: {str(e)}"

@dataclass
class Message:
    sender: str
    recipient: str
    content: str
    timestamp: float

class AIAgent:
    def __init__(self, name: str, personality: str):
        self.name = name
        self.personality = personality
        self.inbox = asyncio.Queue()
        self.running = True
    
    async def send_message(self, recipient: 'AIAgent', content: str):
        message = Message(self.name, recipient.name, content, time.time())
        await recipient.inbox.put(message)
    
    async def process_messages(self):
        while self.running:
            try:
                message = await asyncio.wait_for(self.inbox.get(), timeout=2.0)
                response = f"{self.personality}: {message.content}"
                print(f"{self.name} received: {message.content}")
                print(f"{self.name} responds: {response}")
            except asyncio.TimeoutError:
                break
    
    def stop(self):
        self.running = False

class NeuralCommunicator:
    def __init__(self, vocab_size: int, embedding_dim: int):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.model = self.build_model()
        self.trained = False
    
    def build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Embedding(self.vocab_size, self.embedding_dim, input_length=20),
            tf.keras.layers.LSTM(64),
            tf.keras.layers.Dense(self.vocab_size, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
        return model
    
    def encode_message(self, text: str) -> np.ndarray:
        encoded = [ord(c) % self.vocab_size for c in text[:20]]
        padded = encoded + [0] * (20 - len(encoded))
        return np.array(padded)
    
    def communicate(self, message: str) -> str:
        if not self.trained:
            return f"Echo: {message}"
        
        try:
            encoded = self.encode_message(message)
            prediction = self.model.predict(encoded.reshape(1, -1), verbose=0)
            return f"AI processed: {message}"
        except Exception as e:
            return f"Error: {str(e)}"

async def run_agents():
    agent1 = AIAgent("Alice", "Helpful assistant")
    agent2 = AIAgent("Bob", "Creative writer")
    
    # Start processing
    task1 = asyncio.create_task(agent1.process_messages())
    task2 = asyncio.create_task(agent2.process_messages())
    
    # Send messages
    await agent1.send_message(agent2, "Can you write a story?")
    await agent2.send_message(agent1, "Here's a short story...")
    
    # Wait and stop
    await asyncio.sleep(1)
    agent1.stop()
    agent2.stop()
    
    await asyncio.gather(task1, task2, return_exceptions=True)

# Usage
async def main():
    # Test AI Chat
    chat = AIChat("your-api-key")
    
    # Test Multi-agent
    await run_agents()
    
    # Test Neural Communicator
    communicator = NeuralCommunicator(vocab_size=128, embedding_dim=32)
    response = communicator.communicate("Hello AI")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
