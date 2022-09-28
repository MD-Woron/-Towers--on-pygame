from time import *

import pygame

from init_pg import *
from game_objects import *
"""
BUGS:
1. 
"""
pygame.init()

from load_images import *


while True:
    Game.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                Game.timer = 0
                Game.turn += 1
                Game.boom = Cannon.posy1
        if event.type == pygame.MOUSEBUTTONUP:
            print(event.pos, Game.layers[4][1].get_at(event.pos))
    #if Game.turn%3 == 2:
    #    print(Bullet.x,Bullet.y)
