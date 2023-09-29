import torch
import datetime
from transformers import AutoModelForCausalLM, AutoTokenizer
from langchain import LLMChain

class MemoryObject:
    def __init__(self, description, emotion):  # Added emotion as an argument
        self.created_at = datetime.datetime.now()
        self.last_accessed_at = None
        self.description = description
        self.emotion = emotion  # Added emotion attribute
        self.emotional_state = None

    def access_memory(self):
        self.last_accessed_at = datetime.datetime.now()

class NPC:
    #instantiate NPCs
    def __init__(self, name, temperament, intelligence, description):
        self.name = name
        self.temperament = temperament
        self.intelligence = intelligence
        self.description = description
        self.memory_stream = []
    
    def __str__(self):
        return f"Name: {self.name}\nTemperament: {self.temperament}\nIntelligence: {self.intelligence}\nDescription: {self.description}"

    def add_memory(self, description, emotion):  # Added emotion as an argument
        memory_object = MemoryObject(description, emotion)  # Pass emotion when creating a memory
        self.memory_stream.append(memory_object)

    def retrieve_memories(self, query_emotion, query_relevance):
        # Weigh the recency, importance, and relevance of memories
        weighted_memories = []
        current_time = datetime.datetime.now()

        for memory in self.memory_stream:
            recency_score = 1 - (current_time - memory.created_at).total_seconds() / 3600  # Scale recency to [0, 1]
            
            # Importance score based on emotion similarity and emotional impact
            importance_score = recency_score * (1 if memory.emotion == self.emotional_state else 0.5)
            
            # Relevance score (you can define your relevance logic here)
            relevance_score = query_relevance
            
            # Calculate the total score (you can adjust weights as needed)
            total_score = 0.4 * recency_score + 0.4 * importance_score + 0.2 * relevance_score

            weighted_memories.append((memory, total_score))

        # Sort memories by total score in descending order
        sorted_memories = sorted(weighted_memories, key=lambda x: x[1], reverse=True)

        # Extract the top-ranked memories (e.g., top 3)
        top_ranked_memories = [memory[0] for memory in sorted_memories[:3]]

        return top_ranked_memories

class AIIntegration:
    def __init__(self):
        self.model_name = "gpt2"  # You can change this to a different model
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        self.chain = Chain(self.tokenizer, self.model)

    def generate_response(self, memory_template, user_prompt):
        # Create a memory with the template and user input
        memory = f"{memory_template} {user_prompt}"
        
        # Generate a response using langchain
        response = self.chain.process(memory)
        
        return response