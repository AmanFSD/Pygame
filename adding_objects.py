import pygame
import random

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
player_speed = 2.0

# Falling objects
object_color = (0, 255, 0)  # green color
object_width = 50
object_height = 50
objects = [{"x": random.randrange(screen_width - object_width), "y": 0, "speed": random.random() * 2 + 1} for _ in range(20)]

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

    # Move and draw objects
    for obj in objects:
        obj["y"] += obj["speed"]
        pygame.draw.rect(screen, object_color, pygame.Rect(obj["x"], obj["y"], object_width, object_height))
        # Check for collision with player
        if obj["y"] + object_height > player_y and obj["x"] < player_x + player_width and obj["x"] + object_width > player_x:
            print("Caught object!")
            obj["y"] = 0
            obj["x"] = random.randrange(screen_width - object_width)
            obj["speed"] = random.random() * 2 + 1

    # Draw the player
    screen.fill((0, 0, 0))  # fill screen with black before drawing
    pygame.draw.rect(screen, player_color, pygame.Rect(player_x, player_y, player_width, player_height))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
