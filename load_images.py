from init_pg import WIDTH, HEIGHT
from game_objects import *

def load_image(name):
    if name != 'Пушкам1 правая.png' and name != 'Пушкам1 левая.png':
        image = pygame.image.load(name)
        image = pygame.transform.scale(image, (WIDTH, HEIGHT))
        image.set_colorkey((255, 255, 255))
        image = image.convert_alpha()
    else:
        image = pygame.image.load(name)
        image = pygame.transform.scale(image, (WIDTH*0.08, HEIGHT*0.08))
        image.set_colorkey((255, 255, 255))
        image = image.convert_alpha()
    return image


Game.layers = {
    0: [load_image('Фон.png')],  # Слой 0: Фон
    1: [load_image('Левый Флаг.png'), load_image('Правый флаг.png')],  # Слой 1: Флаги
    2: [load_image('Левая сердцевина.png'), load_image('Правая сердцевина.png')],  # Слой 2: Сердцевины
    3: [Cloud(load_image('Облако1.png'), Game.wind), Cloud(load_image('Облако2.png'), Game.wind),
        Cloud(load_image('Облако3.png'), Game.wind)],  # Слой 3: Облака
    4: [load_image('Левая башня.png'), load_image('Правая башня.png')],  # Слой 4: Разрушающиеся здания
    5: [load_image('Пушкам1 правая.png'), load_image('Пушкам1 левая.png')],  # Слой -1. Пушки.
    6: [load_image('Ядро.png'), load_image('Взрыв.png')]  # Слой 5: Динамический слой
}