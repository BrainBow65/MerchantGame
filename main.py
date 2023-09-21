import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QTextEdit, QDockWidget
from game_world import GameWorld
from npc_manager import AIIntegration

class GameApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Game Application")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a tab widget
        tab_widget = QTabWidget(central_widget)

        # Map Tab
        map_tab = QWidget()
        tab_widget.addTab(map_tab, "Map")
        
        inventory_tab = QWidget()
        tab_widget.addTab(inventory_tab, "Inventory")

        # Sidebar
        sidebar = QDockWidget("Sidebar", self)
        sidebar.setFixedWidth(200)

        sidebar_layout = QVBoxLayout()
        self.sidebar_widget = QTextEdit()
        sidebar_layout.addWidget(self.sidebar_widget)
        sidebar.setWidget(self.sidebar_widget)

        # Create a vertical layout for the central widget
        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(tab_widget)
        main_layout.addWidget(sidebar)

        # Initialize game components
        self.game_world = GameWorld()
        self.npc_manager = NPCManager()

        # Connect NPC interactions to sidebar chat
        self.npc_manager.npc_selected.connect(self.update_sidebar_chat)

    def update_sidebar_chat(self, npc_name):
        # Generate AI response based on selected NPC and user input
        memory_template = f"NPC: {npc_name},"
        user_prompt = self.chat_input.toPlainText()
        ai_response = self.ai_integration.generate_response(memory_template, user_prompt)

        # Update the sidebar chat with AI response
        self.sidebar_widget.append(f"{npc_name}: {ai_response}")
        
        def send_message(self):
        # Handle user sending a message
        selected_npc = self.npc_manager.get_selected_npc()  # Replace with your NPC selection logic
        if selected_npc:
            self.update_sidebar_chat(selected_npc)

def main():
    app = QApplication(sys.argv)
    window = GameApp()
    window.show()
    sys.exit(app.exec_())    

if __name__ == "__main__":
    main()
