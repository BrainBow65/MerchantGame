import sys
import time
import torch
import pygame
from pygame.locals import QUIT, KEYDOWN
from npc_manager import NPC, AIIntegration

class GameApp:
    def __init__(self):
        pygame.init()

        self.window_width = 800
        self.window_height = 600

        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Game Application")

        # Initialize game components
        self.game_world = GameWorld()
        self.npc_manager = NPCManager()

        # Connect NPC interactions to sidebar chat
        self.npc_manager.npc_selected.connect(self.update_sidebar_chat)

        # Initialize AI integration (make sure to pass the correct parameters)
        self.ai_integration = AIIntegration()

        # Initialize fonts
        self.font = pygame.font.Font(None, 36)

        self.city_combo = None
        self.npc_combo = None
        self.chat_input = ""

        self.selected_city = None

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_RETURN:
                        self.send_message()
                    elif event.key == pygame.K_BACKSPACE:
                        self.chat_input = self.chat_input[:-1]
                    else:
                        self.chat_input += event.unicode

            self.screen.fill((255, 255, 255))

            # Render chat input
            input_surface = self.font.render("User: " + self.chat_input, True, (0, 0, 0))
            self.screen.blit(input_surface, (20, self.window_height - 50))

            pygame.display.flip()

        pygame.quit()

    def send_message(self):
        # Get selected language from the dropdown list
        selected_city = self.selected_city

        # Clear the chat input field
        self.chat_input = ""

        # Construct a templated prompt for the LLM
        template = f"You are an intelligent and interesting conversational partner. Respond in a conversational manner to the following and politely correct any grammatical mistakes made by the user: \"{self.chat_input}\" in {selected_city}. Response: "
        prompt = template  # Initial prompt

        # Append conversation history to the prompt
        for message in self.conversation_history:
            prompt += f"User: {message['user']} Bot: {message['bot']} "

        # Encode the prompt using the tokenizer
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)

        # Generate a response using the model
        outputs = self.model.generate(input_ids, max_length=200, num_return_sequences=1)

        # Decode the response
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Update the sidebar chat with AI response
        self.update_sidebar_chat("User", self.chat_input)
        self.update_sidebar_chat("Bot", response)


    def update_sidebar_chat(self, npc_name):
        # Generate AI response based on selected NPC and user input
        memory_template = f"NPC: {npc_name},"
        user_prompt = self.chat_input.toPlainText()  # Replace with the correct input widget
        ai_response = self.ai_integration.generate_response(memory_template, user_prompt)

        # Update the sidebar chat with AI response
        self.sidebar_widget.append(f"{npc_name}: {ai_response}")

        # Implement the send_message method here

class NPCManager:
    def __init__(self):
        # Initialize NPC lists for different cities
        self.city1_npcs = []
        self.city2_npcs = []
        self.city3_npcs = []

        # Populate NPC lists with NPCs for each city
        self.populate_city1_npcs()
        self.populate_city2_npcs()
        self.populate_city3_npcs()

    def populate_city1_npcs(self):
        # Create and add NPCs for City 1 to self.city1_npcs
        self.city1_npcs.append(NPC(name="NPC1 City 1"))
        self.city1_npcs.append(NPC(name="NPC2 City 1"))
        # Add more NPCs as needed

    def populate_city2_npcs(self):
        # Create and add NPCs for City 2 to self.city2_npcs
        self.city2_npcs.append(NPC(name="NPC1 City 2"))
        self.city2_npcs.append(NPC(name="NPC2 City 2"))
        # Add more NPCs as needed

    def populate_city3_npcs(self):
        # Create and add NPCs for City 3 to self.city3_npcs
        self.city3_npcs.append(NPC(name="NPC1 City 3"))
        self.city3_npcs.append(NPC(name="NPC2 City 3"))
        # Add more NPCs as needed

    def get_city1_npcs(self):
        return self.city1_npcs

    def get_city2_npcs(self):
        return self.city2_npcs

    def get_city3_npcs(self):
        return self.city3_npcs

class GameWorld:
    def __init__(self):
        self.npcs = []  # Initialize an empty list of NPCs

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

def main():
    if torch.cuda.is_available():
        torch.set_default_tensor_type(torch.cuda.FloatTensor)
    else:
        print("gpu not available")
    app = QApplication(sys.argv)
    window = GameApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()