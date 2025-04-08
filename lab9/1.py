import pygame, sys
from pygame.locals import *
import random, time


pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock() # for control game's speed

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0  
COIN_SPEED = 3  


font = pygame.font.SysFont("Verdana", 60) #main font
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)   #message "Game over"

background = pygame.image.load("AnimatedStreet.png")

coin_types = [
    {"image": pygame.image.load("BuffCoin.png"), "weight": 3},       # Золото
    {"image": pygame.transform.scale(pygame.image.load("SilverCoin.png"), (176, 176)), "weight": 2},     # Серебро
    {"image": pygame.transform.scale(pygame.image.load("BronzeCoin.png"), (98, 98)), "weight": 1},     # Бронза
] # types of money.Their


DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # create a display
DISPLAYSURF.fill(WHITE) # fill white
pygame.display.set_caption("Game") # caption

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED) # to move enemy
        if self.rect.top > SCREEN_HEIGHT: 
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) # return enemy

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
   def __init__(self):
        super().__init__()
        self.type = random.choice(coin_types)
        self.image = self.type["image"]
        self.weight = self.type["weight"]
        self.rect = self.image.get_rect()
        self.hitbox = self.rect.inflate(-self.rect.width * 0.7, -self.rect.height * 0.7)
        self.reset_position()
   def reset_position(self):
       self.type = random.choice(coin_types)
       self.image = self.type["image"]
       self.weight = self.type["weight"]
       self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), random.randint(-100, -40)))
       self.hitbox = self.rect.inflate(-self.rect.width * 0.7, -self.rect.height * 0.7)
       self.hitbox.center = self.rect.center
    
   def move(self):
        self.rect.move_ip(0, COIN_SPEED)
        self.hitbox.center = self.rect.center
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()




P1 = Player()
E1 = Enemy()
coin = Coin()


enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, coin)





INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.7
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    

    score_display = font_small.render(str(SCORE), True, BLACK)
    coin_display = font_small.render(f"Coins: {COIN_SCORE}", True, BLACK)
    DISPLAYSURF.blit(score_display, (10, 10))
    DISPLAYSURF.blit(coin_display, (SCREEN_WIDTH - 100, 10))
    
   
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        if hasattr(entity, "move"):
            entity.move() 

   
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()


    
    if P1.rect.colliderect(coin.hitbox):
        COIN_SCORE += coin.weight
        coin.reset_position()
    
    pygame.display.update()
    FramePerSec.tick(FPS)
