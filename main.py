import pygame
import ctypes
from math import cos
from math import sin
from math import pi
from random import randint as rnt
from time import time


user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
WIDTH = screensize[0] // 1.5
HEIGHT = screensize[1] // 1.5
FPS = 60
#SCREEN = (screensize[0] // 2, screensize[1] // 2)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()


class Bullet:
    sprite = pygame.Surface((10, 10))
    sprite.fill(WHITE)

    def __init__(self, posx, posy):
        self.x = posx
        self.y = posy

    def change_cords(self, x0, y0, v0, t, alpha):
        self.x = x0 + v0*t*cos(alpha)
        self.y = y0 + v0*t*sin(alpha)-0.5*9.8*t*t


class Game:
    layers = dict()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    wind = rnt(-20, 20)

    def update(self):
        if str(time())[-7] == '0' and str(time())[-9] == '0':
            my_game.wind += rnt(-1, 1)
        for layer in range(5):
            if layer != 3:
                for image in self.layers[layer]:
                    self.screen.blit(image, (0, 0))
            else:
                for image in self.layers[layer]:
                    self.screen.blit(image.sprite, (image.cloud_clock, 0))
                    image.set_clock()
        pygame.display.flip()

    def check_priority(self):
        pass


class Cloud:
    cloud_clock = -1200 - rnt(1,100)

    def __init__(self, sprite, speed):
        self.sprite = sprite
        self.speed = speed + rnt(1, 3)

    def set_clock(self):
        self.speed = my_game.wind
        if self.speed == 0:
            self.speed = 3
        self.cloud_clock += self.speed*0.1
        if self.speed > 0:
            if self.cloud_clock > WIDTH:
                self.cloud_clock = -1200
        elif self.speed < 0:
            if self.cloud_clock < -WIDTH:
                self.cloud_clock = 1300 + rnt(1,100)


my_game = Game()


# Переместить в отдельный моудль
def load_image(name):
    image = pygame.image.load(name)
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    image.set_colorkey((255, 255, 255))
    image = image.convert_alpha()
    return image


my_game.layers = {
    0: [load_image('Фон.jpg')],  # Слой 0: Фон
    1: [load_image('Левый Флаг.jpg'), load_image('Правый флаг.jpg')],  # Слой 1: Флаги
    2: [load_image('Левая штука.jpg'), load_image('Правая штука.jpg')],  # Слой 2: Сердцевины
    3: [Cloud(load_image('Облако1.jpg'), my_game.wind), Cloud(load_image('Облако2.jpg'), my_game.wind),
        Cloud(load_image('Облако3.jpg'), my_game.wind)],  # Слой 3: Облака
    4: [load_image('Левая башня.jpg'), load_image('Правая башня.jpg')],  # Слой 4: Разрушающиеся здания
}
# Переместить в отдельный модуль

#t = 0
#bullet1 = Bullet(100,100)
#test = pygame.transform.scale(pygame.image.load('Фон.jpg'), (WIDTH, HEIGHT))
while True:
    #pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    my_game.update()
    #bullet1.change_cords(10, 500, 100, t, pi / 6)
    #screen.blit(bullet1.sprite, (bullet1.x,700-bullet1.y))
