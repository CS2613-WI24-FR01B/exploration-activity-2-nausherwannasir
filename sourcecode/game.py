import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hockey")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 5

# Puck settings
PUCK_SIZE = 10
PUCK_SPEED_X = 3
PUCK_SPEED_Y = 3

# Game variables
player_score = 0
computer_score = 0

# Create paddles
player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
computer_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create puck
puck = pygame.Rect(WIDTH // 2 - PUCK_SIZE // 2, HEIGHT // 2 - PUCK_SIZE // 2, PUCK_SIZE, PUCK_SIZE)
puck_speed_x = random.choice([-PUCK_SPEED_X, PUCK_SPEED_X])
puck_speed_y = random.choice([-PUCK_SPEED_Y, PUCK_SPEED_Y])

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += PADDLE_SPEED

    # Move computer paddle (simple AI)
    if puck_speed_x > 0 and puck.x > WIDTH // 2:
        if puck.centery < computer_paddle.centery:
            computer_paddle.y -= PADDLE_SPEED
        elif puck.centery > computer_paddle.centery:
            computer_paddle.y += PADDLE_SPEED

    # Move puck
    puck.x += puck_speed_x
    puck.y += puck_speed_y

    # Check puck collisions with walls
    if puck.top <= 0 or puck.bottom >= HEIGHT:
        puck_speed_y = -puck_speed_y

    # Check puck collisions with paddles
    if puck.colliderect(player_paddle) or puck.colliderect(computer_paddle):
        puck_speed_x = -puck_speed_x

    # Check puck out of bounds
    if puck.left <= 0:
        computer_score += 1
        puck = pygame.Rect(WIDTH // 2 - PUCK_SIZE // 2, HEIGHT // 2 - PUCK_SIZE // 2, PUCK_SIZE, PUCK_SIZE)
        puck_speed_x = random.choice([-PUCK_SPEED_X, PUCK_SPEED_X])
        puck_speed_y = random.choice([-PUCK_SPEED_Y, PUCK_SPEED_Y])
    elif puck.right >= WIDTH:
        player_score += 1
        puck = pygame.Rect(WIDTH // 2 - PUCK_SIZE // 2, HEIGHT // 2 - PUCK_SIZE // 2, PUCK_SIZE, PUCK_SIZE)
        puck_speed_x = random.choice([-PUCK_SPEED_X, PUCK_SPEED_X])
        puck_speed_y = random.choice([-PUCK_SPEED_Y, PUCK_SPEED_Y])

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player_paddle)
    pygame.draw.rect(screen, BLUE, computer_paddle)
    pygame.draw.ellipse(screen, BLUE, puck)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
