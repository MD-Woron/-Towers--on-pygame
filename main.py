import pygame

from init_pg import *
from game_objects import *

pygame.init()

from load_images import *

bullet1 = Bullet(0, 0)

game_timer = 0

while True:
    #pygame.time.wait(10)
    Game.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                Game.turn += 1
    if Game.turn%2 == 0:
        Game.screen.blit(bullet1.sprite, (bullet1.x, - bullet1.y))
        pygame.display.flip()
        bullet1.change_cords(0, 0, 100, game_timer, pi / 6)
        game_timer += 0.05

    #bullet1.change_cords(10, 500, 100, t, pi / 6)
    #screen.blit(bullet1.sprite, (bullet1.x,700-bullet1.y))
