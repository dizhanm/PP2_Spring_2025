import pygame
import psycopg2
from random import randrange
import time

def connect():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="dizhan2006",
        host="localhost",
        port="5432"
    )

def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_scores (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        score INTEGER,
        level INTEGER,
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    cur.close()
    conn.close()

def get_or_create_user(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s;", (username,))
    result = cur.fetchone()

    if result:
        user_id = result[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id;", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return user_id

def get_user_level(user_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT level FROM user_scores WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1;", (user_id,))
    result = cur.fetchone()

    cur.close()
    conn.close()
    return result[0] if result else 1

def save_game_state(user_id, score, level):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s);",
        (user_id, score, level)
    )

    conn.commit()
    cur.close()
    conn.close()

# ======== Game Initialization ========
create_tables()

username = input("Please, enter your name: ")
user_id = get_or_create_user(username)
level = get_user_level(user_id)

print(f"Welcome to the game, {username}! Your level is: {level}")

# ======== Game Settings ========
Res = 600
size = 25
score = 0
speed = 3

# Snake initial position
x, y = randrange(0, Res, size), randrange(0, Res, size)
snake = [(x, y)]
length = 1
dx, dy = 0, 0

food = None
food_duration = 5
food_spawn_time = 0
FPS = 10

pygame.init()
sc = pygame.display.set_mode([Res, Res])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_level = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 50, bold=True)
font_food = pygame.font.SysFont('Arial', 12, bold=True)

# Level configurations
level_configs = {
    1: {
        "walls": [],
        "speed": 10
    },
    2: {
        "walls": [(300, 100), (300, 125), (300, 150), (300, 175), (300, 200),
                 (300, 300), (300, 325), (300, 350), (300, 375), (300, 400)],
        "speed": 11
    },
    3: {
        "walls": [(100, 100), (125, 100), (150, 100), (175, 100), (200, 100),
                 (400, 100), (425, 100), (450, 100), (475, 100), (500, 100),
                 (100, 500), (125, 500), (150, 500), (175, 500), (200, 500),
                 (400, 500), (425, 500), (450, 500), (475, 500), (500, 500)],
        "speed": 13
    }
}

def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(sc, pygame.Color('gray'), (*wall, size, size))

# ======== Main Game Loop ========
running = True
while running:
    current_config = level_configs.get(level, level_configs[1])
    sc.fill(pygame.Color('black'))
    FPS = current_config["speed"]
    
    # Draw walls
    draw_walls(current_config["walls"])
    
    # Draw snake
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, size, size))) for i, j in snake]
    
    current_time = time.time()
    
    # Spawn food if needed
    if food is None:
        while True:
            new_food = (
                randrange(0, Res, size),
                randrange(0, Res, size),
                randrange(1, 4)
            )
            if new_food[:2] not in snake and new_food[:2] not in current_config["walls"]:
                food = new_food
                food_spawn_time = current_time
                break
    
    # Remove expired food
    if food and current_time - food_spawn_time > food_duration:
        food = None
    
    # Draw food
    if food:
        x_food, y_food, weight = food
        color = {
            1: pygame.Color('red'),
            2: pygame.Color('orange'),
            3: pygame.Color('purple')
        }.get(weight, pygame.Color('red'))
        
        pygame.draw.rect(sc, color, (*food[:2], size, size))
        weight_text = font_food.render(str(weight), 1, pygame.Color('white'))
        sc.blit(weight_text, (x_food + size//2 - 5, y_food + size//2 - 5))
    
    # Display score and level
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))
    
    render_level = font_level.render(f'LEVEL: {level}', 1, pygame.Color('white'))
    sc.blit(render_level, (5, 35))

    # Move snake
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
        food = None
        
        # Level progression based on length
        if level == 1 and length >= 5:
            level = 2
        elif level == 2 and length >= 10:
            level = 3
            
    
    # Game over conditions
    if (x < 0 or x > Res - size or 
        y < 0 or y > Res - size or 
        len(snake) != len(set(snake)) or
        (x, y) in current_config["walls"]):
        
        save_game_state(user_id, score, level)
        
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            sc.blit(render_end, (Res//2 - 150, Res//3))
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
    
    pygame.display.flip()
    clock.tick(FPS)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game_state(user_id, score, level)
            exit()
    
    # Keyboard controls
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and dy != 1:
        dx, dy = 0, -1
    if key[pygame.K_DOWN] and dy != -1:
        dx, dy = 0, 1
    if key[pygame.K_LEFT] and dx != 1:
        dx, dy = -1, 0
    if key[pygame.K_RIGHT] and dx != -1:
        dx, dy = 1, 0