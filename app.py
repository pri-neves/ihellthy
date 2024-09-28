import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 250, 154)
PINK = (255,20,147)
RED = (255,0,0)
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCORE = "0"
gameState = "start"
bg_image1 = pygame.image.load('assets/images/fundo1.jpg')
bg_image2 = pygame.image.load('assets/images/fundo2.jpg')
bg_image1 = pygame.transform.scale(bg_image1,(SCREEN_WIDTH,SCREEN_HEIGHT))
apple = pygame.image.load('assets/images/apple.png')
apple = pygame.transform.scale(apple,(60,60))
pizza = pygame.image.load('assets/images/pizza.png')
pizza = pygame.transform.scale(pizza,(70,70))
cesta = pygame.image.load('assets/images/cesta.png')

cesta = pygame.transform.scale(cesta,(100,50))
sum = 0
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([150, 15])
        self.image = cesta
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
 
    def update(self):
        self.rect.x += self.change_x
 
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
 
        self.rect.y += self.change_y
 
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class EnemyFood(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image = pizza
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, y):
        self.change_y += y
 
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        


class HealthyFood(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image = apple
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, y):
        self.change_y += y
 
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y



 
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

def draw_start_menu():
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont('arial', 30)
   start_button = font.render('Press S to Start', True, (255, 255, 255))
   about = font.render('Press A to About Game', True, (255, 255, 255))
   screen.blit(start_button, (SCREEN_WIDTH/2 - start_button.get_width()/2, SCREEN_HEIGHT/2 + start_button.get_height()/2))
   screen.blit(about, (SCREEN_WIDTH/2 - about.get_width()/2, SCREEN_HEIGHT/2 - about.get_height()/2))
   pygame.display.update()
   
def draw_about_game():
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont('arial', 20)
   about = font.render('Esse jogo é sobre alimentação Saudável. Hellthy é um trocadilho com as palavras Hell e Healthy', True, (255, 255, 255))
   quit_button = font.render('Pressione Q para voltar para o MENU', True, (255, 255, 255))
   screen.blit(about, (SCREEN_WIDTH/2 - about.get_width()/2, SCREEN_HEIGHT/3 - about.get_height()/3))
   screen.blit(quit_button, (SCREEN_WIDTH/2 - quit_button.get_width()/2, SCREEN_HEIGHT/2 - quit_button.get_height()/2))
   pygame.display.update()

pygame.init()
 
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
pygame.display.set_caption('I Hellthy')


all_sprite_list = pygame.sprite.Group()
 
wall_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(790, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
 
player = Player(325, 500)
player.walls = wall_list
 
all_sprite_list.add(player)

clock = pygame.time.Clock()
 
done = False
listEnemyFoods = pygame.sprite.Group()
listHealthyFoods = pygame.sprite.Group()

enemy = EnemyFood(random.randrange(10,750),random.randrange(10,300))
listEnemyFoods.add(enemy)

food = HealthyFood(random.randrange(10,750),random.randrange(10,300))
listHealthyFoods.add(food)

all_sprite_list.add(listEnemyFoods)
all_sprite_list.add(listHealthyFoods)
font = pygame.font.SysFont('Arial',26)
text = font.render('Pontuação: ',True,PINK)

#points = font.render(SCORE,True,BLUE)
foods_hit_list = pygame.sprite.spritecollide(player,listHealthyFoods,True)
enemies_hit_list = pygame.sprite.spritecollide(player,listEnemyFoods,True)

while not done:
    screen.fill(BLACK)
    if sum > 10:
        screen.blit(bg_image2,(0,0))
    else:
        screen.blit(bg_image1,(0,0))
    points = font.render(SCORE,True,BLUE)
    screen.blit(text,(400,20))
    screen.blit(points,(530,20))

    if gameState == "start":
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            gameState = "game"
        elif keys[pygame.K_a]:
            gameState = "about"
    if gameState == "about":
        draw_about_game()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            gameState = "start"
    if gameState == "game":
        if (pygame.time.get_ticks()) % 250 == 0:
            enemy = EnemyFood(random.randrange(10,750),random.randrange(10,300))
            listEnemyFoods.add(enemy)
            all_sprite_list.add(listEnemyFoods)

        if (pygame.time.get_ticks()) % 100 == 0:
            food = HealthyFood(random.randrange(10,750),random.randrange(10,300))
            listHealthyFoods.add(food)
            all_sprite_list.add(listHealthyFoods)

        for obj in listEnemyFoods:
            obj.changespeed(0.01)
            if pygame.sprite.collide_rect(obj,player):
                obj.kill()
                sum = int(SCORE) - 1
                SCORE = str(sum)

        for obj in listHealthyFoods:
            obj.changespeed(0.015)
            if pygame.sprite.collide_rect(obj,player):
                obj.kill()
                sum = int(SCORE) + 1
                SCORE = str(sum)

        for food in foods_hit_list:
            sum = int(score) + 1
            score = str(sum)
        all_sprite_list.update()
 
        all_sprite_list.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #done = True
            pygame.quit()
            quit()
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)


    
 
    
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()