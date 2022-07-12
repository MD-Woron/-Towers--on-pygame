def set_size(text, color):
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    return tuple(map(int, text.split()))
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
                screen.fill((30, 30, 30))
                text_surface = font.render(text, True, color)
                screen.blit(text_surface, (50, 100))
                pygame.display.flip()

import pygame
import ctypes
from math import cos
from math import sin
from math import pi

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
WIDTH = screensize[0] // 1.5
HEIGHT = screensize[1] // 1.5
FPS = 60
SCREEN = (screensize[0] // 2, screensize[1] // 2)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()

font_color = pygame.Color('dodgerblue2')

pygame.display.set_caption('Введите размер поля (x y)')
font = pygame.font.SysFont('arial', 64)
text = ''

screen = pygame.display.set_mode((WIDTH, HEIGHT))
field_size = (10,10)#set_size(text, font_color)


class Player():
    sprite = {}

    def __init__(self, posx, posy):
        for x in range(posx-50, posx):
            for y in range(posy,posy-30,-1):
                brick = pygame.Surface((10,10))
                brick.fill(RED)
                self.sprite[(x,y)] = brick

    def player_blit(self):
        for elem in self.sprite.keys():
            screen.blit(self.sprite[elem], elem)

class Bullet():
    sprite = pygame.Surface((10,10))
    sprite.fill(WHITE)

    def __init__(self, posx, posy):
        self.x = posx
        self.y = posy

    def change_cords(self,x0, y0, v0, t, alpha,):
        self.x = x0 + v0*t*cos(alpha)
        self.y = y0 + v0*t*sin(alpha)-0.5*9.8*t*t


t = 0
player1 = Player(310, 210)
player2 = Player(710, 210)
bullet1 = Bullet(100,100)

while True:
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    t += 0.1
    bullet1.change_cords(10, 500, 100, t, pi / 6)
    screen.fill(BLACK)
    screen.blit(bullet1.sprite, (bullet1.x,700-bullet1.y))
    player1.player_blit()
    player2.player_blit()
    pygame.display.flip()
