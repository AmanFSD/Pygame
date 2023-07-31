import pygame

# Initialize Pygame
pygame.init()

# Set up some variables for the screen
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Player character
player_width = 60
player_height = 80
player_x = screen_width / 2  # start at middle of screen
player_y = screen_height - player_height  # start at bottom of screen
player_color = (255, 0, 0)  # RGB color for red

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the player
    pygame.draw.rect(screen, player_color, pygame.Rect(player_x, player_y, player_width, player_height))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
