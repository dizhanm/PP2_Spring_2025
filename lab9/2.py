import pygame
from random import randrange
import time

Res = 600
size = 25
score = 0
speed = 3

# snake position
x, y = randrange(0, Res, size), randrange(0, Res, size)
snake = [(x, y)] # list to hold snake coordinates
length = 1
dx, dy = 0, 0 # direction of movement

food = None
food_duration = 5  # how long the food stays on screen in seconds
food_spawn_time = 0  # time when food was spawned

FPS = 10  # speed of the game 
pygame.init()
sc = pygame.display.set_mode([Res, Res])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True) # for score
font_end = pygame.font.SysFont('Arial', 50, bold=True) # for "Game Over"
font_food = pygame.font.SysFont('Arial', 12, bold=True) # for food weight text

running = True
while running:
    sc.fill(pygame.Color('black'))
    
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, size, size))) for i, j in snake] # Draw the snake
    
    current_time = time.time()
    
    if food is None:  # Spawn food 
        new_food = (
            randrange(0, Res, size),
            randrange(0, Res, size),
            randrange(1, 4)
        )
        if new_food[:2] not in snake:
            food = new_food
            food_spawn_time = current_time # when food appeared
    
    # Remove food if time exceeded
    if food and current_time - food_spawn_time > food_duration:
        food = None
    
    # Draw the food 
    if food:
        x_food, y_food, weight = food
        color = {
            1: pygame.Color('red'),
            2: pygame.Color('orange'),
            3: pygame.Color('purple')
        }.get(weight, pygame.Color('red'))
        
        pygame.draw.rect(sc, color, (*food[:2], size, size))  # draw food square
        weight_text = font_food.render(str(weight), 1, pygame.Color('white')) # draw food value
        sc.blit(weight_text, (x_food + size//2 - 5, y_food + size//2 - 5))  # center the number
    
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5)) # Display score

    # Move the snake
    x += dx * size
    y += dy * size
    snake.append((x, y))
    snake = snake[-length:]
    

     # Check if snake eats food
    if food and snake[-1] == food[:2]:
        x_food, y_food, weight = food
        length += weight
        FPS += 0.5 * weight
        score += weight
        food = None # remove the eaten food
    
    if (x < 0 or x > Res - size or 
        y < 0 or y > Res - size or 
        len(snake) != len(set(snake))): # if snake hits itself
        
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            sc.blit(render_end, (Res//2 - 150, Res//3))
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
    
    pygame.display.flip()
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and dy != 1: # move up
        dx, dy = 0, -1
    if key[pygame.K_DOWN] and dy != -1: # move down
        dx, dy = 0, 1
    if key[pygame.K_LEFT] and dx != 1: # move left
        dx, dy = -1, 0
    if key[pygame.K_RIGHT] and dx != -1: # move right
        dx, dy = 1, 0