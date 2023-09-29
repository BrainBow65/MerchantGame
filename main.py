import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PC_SIZE = 50
PC_SPEED = 5
BACKGROUND_COLOR = (255, 255, 255)
PC_IMAGE = pygame.image.load("PC_sprite.jpeg")
BACKGROUND_IMAGE = pygame.image.load("background.jpeg")
SHOP_IMAGE = pygame.image.load("shop_image.jpeg")
BUTTON_COLOR = (0, 128, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving PC")

# Initial PC position
pc_x = (WIDTH - PC_SIZE) // 2
pc_y = (HEIGHT - PC_SIZE) // 2

# Shop window flag
show_shop_window = False

# Define font
font = pygame.font.Font(None, 36)

# Buttons
yes_button_rect = pygame.Rect(200, 450, 100, 50)
no_button_rect = pygame.Rect(500, 450, 100, 50)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button clicked
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if yes_button_rect.collidepoint(mouse_x, mouse_y):
                    show_shop_window = False  # Player clicked "Yes"
                elif no_button_rect.collidepoint(mouse_x, mouse_y):
                    show_shop_window = False  # Player clicked "No"

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

    # Check if the PC is in front of the SHOP_IMAGE
    pc_rect = pygame.Rect(pc_x, pc_y, PC_SIZE, PC_SIZE)
    shop_rect = pygame.Rect(WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2)

    if pc_rect.colliderect(shop_rect):
        show_shop_window = True
    else:
        show_shop_window = False

    # Fill the screen with the background color and draw the background image
    screen.fill(BACKGROUND_COLOR)
    screen.blit(BACKGROUND_IMAGE, (0, 0))

    # Draw the SHOP_IMAGE
    screen.blit(SHOP_IMAGE, (WIDTH // 4, HEIGHT // 4))

    # Draw the PC image at its current position
    screen.blit(PC_IMAGE, (pc_x, pc_y))

    # Display the shop window if necessary
    if show_shop_window:
        pygame.draw.rect(screen, (0, 0, 0), (0, HEIGHT - 100, WIDTH, 100))  # Draw a black bar at the bottom
        text = font.render("Do you want to enter the shop? (Y/N)", True, (255, 255, 255))
        screen.blit(text, (10, HEIGHT - 80))
        pygame.draw.rect(screen, BUTTON_COLOR, yes_button_rect)
        pygame.draw.rect(screen, BUTTON_COLOR, no_button_rect)
        yes_text = font.render("Yes", True, BUTTON_TEXT_COLOR)
        no_text = font.render("No", True, BUTTON_TEXT_COLOR)
        screen.blit(yes_text, (yes_button_rect.centerx - yes_text.get_width() // 2, yes_button_rect.centery - yes_text.get_height() // 2))
        screen.blit(no_text, (no_button_rect.centerx - no_text.get_width() // 2, no_button_rect.centery - no_text.get_height() // 2))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()