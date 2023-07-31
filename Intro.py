import pygame

# Initialize Pygame
pygame.init()

# Set up some variables for the screen
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

# Quit Pygame
pygame.quit()
