import time

class GameWorld:
    def __init__(self, npcs):
        self.npcs = npcs  # List of NPCs

    def start_game_loop(self):
        timestep = 0
        while True:
            print(f"Timestep {timestep}")
            
            # Update the emotional state for each NPC
            for npc in self.npcs:
                npc.update_emotional_state()
                print(f"Emotional State of {npc.name}: {npc.emotional_state}")
            
            # Simulate a delay for the timestep
            time.sleep(1)  # Adjust the delay as needed
            
            timestep += 1


if __name__ == "__main__":
    from npc_manager import NPC  # Import the NPC class from your NPC module

    npc1 = NPC(
        name="John",
        temperament="Friendly",
        intelligence="Average",
        description="John is a friendly and outgoing individual. He enjoys working as a baker in the town's bakery during the day and playing music at the local tavern in the evenings. He has a close relationship with NPC2 and often shares stories from their adventures."
    )

    npc2 = NPC(
        name="Alice",
        temperament="Reserved",
        intelligence="High",
        description="Alice is known for her reserved nature but incredible intelligence. She works as the town's librarian, where she spends most of her time surrounded by books. She is an avid chess player and enjoys challenging NPC3 to strategic matches."
    )

    npc3 = NPC(
        name="Bob",
        temperament="Adventurous",
        intelligence="Above Average",
        description="Bob is an adventurous spirit who loves exploring the wilderness around the town. He works as a ranger and often goes on expeditions to protect the town from threats. He has a strong camaraderie with NPC1 and often joins in the bakery's celebrations after returning from an adventure."
    )

    npcs = [npc1, npc2, npc3]

    game_world = GameWorld(npcs)
    game_world.start_game_loop()

