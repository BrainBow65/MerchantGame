# MerchantGame
This is a proof of concept language learning game application powered by open source AI
The game world will be populated by a limited number of AI generative agents based on the architecture described in this paper
- Park, J.S., O’Brien, J.C., Cai, C.J., Morris, M.R., Liang, P., Bernstein, M.S., 2023. Generative Agents: Interactive Simulacra of Human Behavior. https://doi.org/10.48550/arXiv.2304.03442

The game loop consists of the player traveling to different cities with items acquired in a different area and selling them at a profit. The bartering will be the drive to communicate with the agents as the better relationship the player has with them the more profit they can generate.
They will progress in the game by being able to buy bigger inventory upgrades, getting access to rarer/ more valuable materials, and improving relationships with artisans who can process raw materials into more valuable items.

---
To run this program you need to have these packages installed
- PySide
- dotenv
- huggingfacehub
- langchain
- pytorch
---
## AI Driven Translation
The AI agents will act based on prompts fed to an LLM and their memories will be tracked by a memory stream list and retrieved based on relevance.
The LLm will generate conversation which will be fed to a translator AI for the desired target language. Ideally a voice to text input for the player and a text to voice implementation for the AI responses to practice listening comprehension and speech. Until then only text input and generation will be displayed.

## Want to try and use BLOOM LLM
- It is a multilingual model in its own right so I wouldn't have to translate the answers give, eliminating an unnecessary step

---
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/BrainBow65)
