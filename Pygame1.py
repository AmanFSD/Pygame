import pygame
import sys

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
BALL_DIAMETER = 15
BALL_RADIUS = BALL_DIAMETER // 2
BRICK_WIDTH = 60
BRICK_HEIGHT = 15
PADDLE_Y = SCREEN_HEIGHT - PADDLE_HEIGHT - 10
BALL_Y = PADDLE_Y - BALL_DIAMETER
BRICK_Y = 50
BRICKS_PER_ROW = SCREEN_WIDTH // BRICK_WIDTH
NBRICK_ROWS = 5

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE=(255,255,255)


# Paddle Class
class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, speed):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-speed, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(speed, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH


# Ball Class
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, BALL_Y, BALL_DIAMETER, BALL_DIAMETER)
        self.speed = [5, -5]

    def move(self):
        self.rect.move_ip(self.speed)

        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed[0] *= -1
        if self.rect.top < 0:
            self.speed[1] *= -1


# Brick Class
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Create Game Objects
paddle = Paddle()
ball = Ball()
bricks = pygame.sprite.Group()
colors = [RED, GREEN, BLUE]

for row in range(NBRICK_ROWS):
    brick_color = colors[row % len(colors)]
    brick_y = BRICK_Y + (BRICK_HEIGHT * row)
    for brick_x in range(0, SCREEN_WIDTH, BRICK_WIDTH):
        brick = Brick(brick_x, brick_y, brick_color)
        bricks.add(brick)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Draw Paddle
    pygame.draw.rect(screen, RED, paddle.rect)
    paddle.move(5)

    # Draw Ball
    pygame.draw.ellipse(screen, WHITE, ball.rect)
    ball.move()

    # Draw Bricks
    bricks.draw(screen)

    # Check for collisions
    if paddle.rect.colliderect(ball.rect):
        ball.speed[1] *= -1

    hit_brick = pygame.sprite.spritecollideany(ball, bricks)
    if hit_brick:
        bricks.remove(hit_brick)
        ball.speed[1] *= -1

    if ball.rect.bottom > SCREEN_HEIGHT:
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
