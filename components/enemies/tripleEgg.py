import random
import pygame
from utils.consts import WIDTH, HEIGHT, BASEDIR
from components.enemies.egg import Egg

class TripleEgg(Egg):
    def __init__(self, spawn, radius, radiusDrawn=False):
        Egg.__init__(self, spawn, radius, radiusDrawn)
        self.image = pygame.image.load(f'{BASEDIR}\\assets\\eggs\\tripleEgg.png')

    def onEat(self, player):
        player.score += 3
        player.stamina += 10 if player.stamina < player.staminaLimit else 0
        self.kill()
