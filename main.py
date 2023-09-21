import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

# Set up game variables
snake_position = [[100, 50], [90, 50], [80, 50]]
food_position = [random.randrange(1, width//10) * 10, random.randrange(1, height//10) * 10]
score = 0
direction = 'RIGHT'
change_to = direction

# Set up game clock
clock = pygame.time.Clock()
snake_speed = 15

# Game Over function
def game_over():
    font = pygame.font.SysFont('Arial', 30)
    game_over_text = font.render("Game Over!", True, red)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.midtop = (width / 2, height / 4)
    window.blit(game_over_text, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    quit()

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'

    # Validate direction change
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    # Update snake position
    if direction == 'RIGHT':
        snake_position[0][0] += 10
    if direction == 'LEFT':
        snake_position[0][0] -= 10
    if direction == 'UP':
        snake_position[0][1] -= 10
    if direction == 'DOWN':
        snake_position[0][1] += 10

    # Snake body collision check
    for block in snake_position[1:]:
        if snake_position[0] == block:
            game_over()

    # Create food and increase score
    if snake_position[0] == food_position:
        score += 1
        food_position = [random.randrange(1, width//10) * 10, random.randrange(1, height//10) * 10]
        snake_position.append([0, 0])

    # Boundary check
    if snake_position[0][0] >= width or snake_position[0][0] < 0 or snake_position[0][1] >= height or snake_position[0][1] < 0:
        game_over()

    # Update the game window
    window.fill(black)
    for pos in snake_position:
        pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(window, red, pygame.Rect(food_position[0], food_position[1], 10, 10))

    # Update snake body positions
    snake_body = snake_position[:-1]
    snake_body.insert(0, list(snake_position[0]))
    snake_position = snake_body[:]

    # Refresh game display
    pygame.display.flip()

    # Set game speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
