import pygame 
import random 
import time 
pygame.init() 
 
pygame.display.set_caption('Crash') 
 
W=400 
H=600 
  
sc=pygame.display.set_mode((W, H)) 
 
BLUE=(0, 0, 255) 
RED=(255, 0, 0) 
GREEN=(0, 255, 0) 
BLACK=(0, 0, 0) 
WHITE=(255, 255, 255) 
  
sc.fill(WHITE) 
#we define the minimum and maximum weights of the coins
MIN_WEIGHT = 2
MAX_WEIGHT = 10 

#we define the initial speed of the enemy and the number of coins to increase its speed
INITIAL_ENEMY_SPEED = 1
COINS_TO_INCREASE_SPEED = 5

#We define a variable to keep track of the number of coins collected by the player
player_coins  = 0

#We define a variable to keep track of the current enemy speed
enemy_speed = INITIAL_ENEMY_SPEED
clock=pygame.time.Clock() 
 
SPEED=5 
SCORE=0 
SCORE1=0 
 
pygame.mixer.music.load('background.wav') 
pygame.mixer.music.play(-1) 
 
font=pygame.font.SysFont("Verdana", 60) 
font_small=pygame.font.SysFont("Verdana", 20) 
game_over=font.render("Game Over", True, BLACK) 
  
background=pygame.image.load("AnimatedStreet.png") 
  
sc=pygame.display.set_mode((W, H)) 
sc.fill(WHITE) 
  
class Enemy(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__()  
        self.image=pygame.image.load("Enemy.png") 
        self.rect=self.image.get_rect() 
        self.rect.center=(random.randint(40, W-40), 0)   
  
    def move(self): 
        global SCORE 
        self.rect.move_ip(0, SPEED) 
        if (self.rect.top>600): 
            SCORE+=1 
            self.rect.top=0 
            self.rect.center=(random.randint(40, W-40), 0) 
 
class Coin(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() 
        self.image=pygame.image.load("Coin.png") 
        self.rect=self.image.get_rect() 
        self.rect.center=(random.randint(40, W-40), 0)   
        self.image.set_colorkey((WHITE)) 
 
    def move(self): 
        global SCORE1 
        self.rect.move_ip(0, SPEED) 
        if(self.rect.bottom>600): 
            self.rect.top=0 
            self.rect.center=(random.randint(40, W-40), 0) 
        elif Collide(): 
            SCORE1+=1 
            self.rect.top=0 
            self.rect.center=(random.randint(self.rect.width, H-self.rect.width), 0) 
    #We define a function to generate a random coin with a random weight
    def generate_coin():
      weight = random.randint(MIN_WEIGHT, MAX_WEIGHT)
      return weight
    #We define the main game loop
    if True:
# We generate a new coin and update the player's coin count
     coin_weight = generate_coin()
     player_coins += 1
class Player(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__()  
        self.image=pygame.image.load("Player.png") 
        self.rect=self.image.get_rect() 
        self.rect.center=(160, 520) 
         
    def move(self): 
        pressed_keys=pygame.key.get_pressed()   
        if self.rect.left>0: 
              if pressed_keys[pygame.K_LEFT]: 
                  self.rect.move_ip(-5, 0) 
        if self.rect.right<W:         
              if pressed_keys[pygame.K_RIGHT]: 
                  self.rect.move_ip(5, 0) 
                            
P1=Player() 
E1=Enemy() 
C1=Coin() 
 
enemies=pygame.sprite.Group() 
enemies.add(E1) 
coins=pygame.sprite.Group() 
coins.add(C1) 
all_sprites=pygame.sprite.Group() 
all_sprites.add(P1) 
all_sprites.add(E1) 
all_sprites.add(C1) 
  
INC_SPEED=pygame.USEREVENT+1 
pygame.time.set_timer(INC_SPEED, 1000) 
 
def Collide(): 
    if pygame.sprite.spritecollideany(P1,coins): 
        return True 
    else: 
        return False 
 
while True: 
    for event in pygame.event.get(): 
        if event.type==INC_SPEED: 
            SPEED+=0.5      
        if event.type==pygame.QUIT: 
            exit() 
  
    sc.blit(background, (0, 0)) 
    scores=font_small.render(str(SCORE), True, BLACK) 
    sc.blit(scores, (10, 10)) 
     
    scores1=font_small.render(str(SCORE1), True, BLACK) 
    sc.blit(scores1, (380, 10)) 
 
    for entity in all_sprites: 
        sc.blit(entity.image, entity.rect) 
        entity.move() 
 
    if coins==enemies: 
        False 
 
    if pygame.sprite.spritecollideany(P1, enemies): 
        pygame.mixer.Sound('crash.wav').play() 
        time.sleep(0.5) 
                     
        sc.fill(RED) 
        sc.blit(game_over, (30,250)) 
            
        pygame.display.update() 
        for entity in all_sprites: 
            entity.kill()  
            time.sleep(2) 
        exit()
    

    pygame.display.update() 
    clock.tick(60)