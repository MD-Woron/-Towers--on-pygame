import pygame
from init_pg import *
from random import randint as rnt
from time import time
from math import cos
from math import sin
from math import pi


class Bullet:
    sprite = None
    explosion = None

    def __init__(self, posx, posy):
        self.x = posx
        self.y = posy

    def change_cords(self, x0, y0, v0, t, alpha):
        self.x = x0 + v0*t*cos(alpha)
        self.y = y0 + v0*t*sin(alpha)-0.5*10*t*t


class Game:
    turn = -1 # чёт - первый игрок, нечет - второй игрок
    layers = dict()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    wind = rnt(-20, 20)

    @classmethod
    def update(cls):
        if str(time())[-7] == '0' and str(time())[-9] == '0':
            Game.wind += rnt(-1, 1)
        for layer in cls.layers.keys():
            if layer not in (3, 6):
                for image in cls.layers[layer]:
                    cls.screen.blit(image, (0, 0))
            elif layer == 3:
                for image in cls.layers[layer]:
                    cls.screen.blit(image.sprite, (image.cloud_clock, 0))
                    image.set_clock()
            elif layer == 6:
                Bullet.sprite = cls.layers[6][0]
                Bullet.explosion = cls.layers[6][1]

        pygame.display.flip()

    def check_priority(self):
        pass


class Cloud:
    cloud_clock = -1200 - rnt(1, 100)

    def __init__(self, sprite, speed):
        self.sprite = sprite
        self.speed = speed + rnt(1, 3)

    def set_clock(self):
        self.speed = Game.wind
        if self.speed == 0:
            self.speed = 3
        self.cloud_clock += self.speed*0.1
        if self.speed > 0:
            if self.cloud_clock > WIDTH:
                self.cloud_clock = -1200
        elif self.speed < 0:
            if self.cloud_clock < -WIDTH:
                self.cloud_clock = 1300 + rnt(1, 100)
