from init_pg import *
from random import randint as rnt
from time import time
from math import cos
from math import sin
from math import pi

class Game:
    timer = 0
    turn = 1
    layers = dict()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    wind = rnt(-20, 20)
    flag = True
    boom = 0

    @classmethod
    def update(cls):
        if str(time())[-7] == '0' and str(time())[-9] == '0':
            cls.wind += rnt(-1, 1)
        for layer in cls.layers.keys():
            if layer not in (3,5,6):
                for image in cls.layers[layer]:
                    cls.screen.blit(image, (0, 0))
            elif layer == 3:
                for image in cls.layers[layer]:
                    cls.screen.blit(image.sprite, (image.cloud_clock, 0))
                    image.set_clock()
            elif layer == 6:
                #cls.layers[5][0] = pygame.transform.rotate(cls.layers[5][0], 1)
                if Cannon.posy1 < 600 and cls.flag:
                    Cannon.posy1 += 1
                    Cannon.posy2 += 1
                elif Cannon.posy1 >= 357:
                    cls.flag = False
                    Cannon.posy1 -= 1
                    Cannon.posy2 -= 1
                else:
                    cls.flag = True
                #cls.layers[5][1] = pygame.transform.rotate(cls.layers[5][1], 1)
                if cls.turn%4 == 2:
                    Bullet.set_cords(0, 0)
                    Bullet.change_cords(0, 0, 100, cls.timer, pi / 6)
                    cls.screen.blit(Bullet.sprite, (Bullet.x, - Bullet.y - 357 + Game.boom))
                    cls.timer += 0.2
                if cls.turn > 0 and cls.turn%4 == 0:
                    Bullet.set_cords(750, 0)
                    Bullet.change_cords(750, 0, 100, cls.timer, pi - pi / 6)
                    cls.screen.blit(Bullet.sprite, (Bullet.x, - Bullet.y - 357 + Game.boom))
                    cls.timer += 0.2
            elif layer == 5:
                cls.screen.blit(cls.layers[layer][0], (Cannon.posx2, Cannon.posy2))
                cls.screen.blit(cls.layers[layer][1], (Cannon.posx1, Cannon.posy1))

        pygame.display.flip()

    @classmethod
    def check_priority(cls, posx, posy):
        left_tower, right_tower = cls.layers[4]
        if Game.turn%4 == 2:
            try:
                color = right_tower.get_at((posx+190, -posy+Game.boom-25))
                print(posx,-posy)
                if color[3] > 0:
                    tmp = color
                    tmp[3] = 0
                    for x in range(20):
                        for y in range(20):
                            right_tower.set_at((posx+190+x, -posy+Game.boom-25+y), tmp)
                    Game.turn += 1
                    Game.timer = 0
            except IndexError: pass
        if Game.turn%4 == 0:
            try:
                color = left_tower.get_at((posx+190, -posy+Game.boom))
                print(posx,-posy)
                if color[3] > 0:
                    tmp = color
                    tmp[3] = 0
                    for x in range(20):
                        for y in range(20):
                            left_tower.set_at((posx+190+x, -posy+Game.boom+y), tmp)
                    Game.turn += 1
                    Game.timer = 0
            except IndexError: pass





class Cannon:
    posx1 = 150
    posx2 = 1020
    posy1 = 357
    posy2 = 357

class Bullet:
    @classmethod
    def set_cords(cls, posx, posy):
        cls.x = posx
        cls.y = posy
        cls.sprite = Game.layers[6][0]
        cls.explosion = Game.layers[6][1]
        if Game.timer <= 1:
            Game.screen.blit(cls.explosion, (Bullet.x + 30*(Game.turn%3 == 0), - Bullet.y - 357 + Game.boom))
    @classmethod
    def change_cords(cls, x0, y0, v0, t, alpha):
        cls.x = round(x0 + v0*t*round(cos(alpha),3))
        cls.y = round(y0 + v0*t*round(sin(alpha),3)-0.5*10*t*t)
        Game.check_priority(int(cls.x), int(cls.y))


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
