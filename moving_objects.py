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
player_x = screen_width / 2
player_y = screen_height - player_height
player_color = (255, 0, 0)
player_speed = 2.0  # new variable for the player speed

# Game Loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Draw the player
    screen.fill((0, 0, 0))  # fill screen with black before drawing to prevent smearing effect
    pygame.draw.rect(screen, player_color, pygame.Rect(player_x, player_y, player_width, player_height))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
