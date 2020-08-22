import pygame
import random

#Screen
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Game Screen")
icon = pygame.image.load('images/rocket.png')
pygame.display.set_icon(icon)
background = pygame.image.load('images/background.jpg')

# Player
player = pygame.image.load('images/spaceship.png')
player_x = 660
player_y = 600
player_x_change = 0
player_y_change = 0
player_speed = 10

# Enemy


enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = [3.5, -3.5, 3.5, -3.5, 3.5, -3.5]
enemy_y_change = []
num_of_enemies = 6
enemy_base_speed = 4


def enemies(n = 6):
    global enemy_x_change
    for i in range(num_of_enemies):
        enemy.append(pygame.image.load("images/evil.png"))
        enemy_x.append(random.randint(25, 1215))
        enemy_y.append(random.randint(25, 300))
        enemy_y_change.append(64)
        try:
            if enemy_x_change[i] < 0:
                enemy_x_change[i] -= 0.5
                print(1)
            else:
                enemy_x_change[i] += 0.5
                print(2)
        except IndexError:
            enemy_x_change.append(enemy_base_speed)
            print(3)

def enemyShow(x, y, i):
    screen.blit(enemy[i], (x, y))
# Bullet
bullet = pygame.image.load("images/bullet.png")
bullet_x = -40
bullet_y = 576
bullet_y_change = 10
charge = 'ready'

# Score
pygame.font.init()
score_value = 0
font = pygame.font.Font('images/Dead Revolution.otf', 32)

text_x = 10
test_y = 10

# Game Over
over_font = pygame.font.Font('images/Dead Revolution.otf', 128)