import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PC_SIZE = 50
PC_SPEED = 5
BACKGROUND_COLOR = (255, 255, 255)
PC_IMAGE = pygame.image.load("pc_image.png")
BACKGROUND_IMAGE = pygame.image.load("background_image.png")

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving PC")

# Initial PC position
pc_x = (WIDTH - PC_SIZE) // 2
pc_y = (HEIGHT - PC_SIZE) // 2

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get a list of the keys that are currently pressed
    keys = pygame.key.get_pressed()

    # Move the PC based on user input
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        pc_x -= PC_SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        pc_x += PC_SPEED
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        pc_y -= PC_SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        pc_y += PC_SPEED

    # Ensure the PC stays within the screen boundaries
    pc_x = max(0, min(pc_x, WIDTH - PC_SIZE))
    pc_y = max(0, min(pc_y, HEIGHT - PC_SIZE))

    # Fill the screen with the background color and draw the background image
    screen.fill(BACKGROUND_COLOR)
    screen.blit(BACKGROUND_IMAGE, (0, 0))

    # Draw the PC image at its current position
    screen.blit(PC_IMAGE, (pc_x, pc_y))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
