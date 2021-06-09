import random
import pygame
from utils.consts import WIDTH, HEIGHT, BASEDIR
from components.enemies.egg import Egg

class BombEgg(Egg):
    def __init__(self, spawn, radius, radiusDrawn=False):
        Egg.__init__(self, spawn, radius, radiusDrawn)
        self.image = pygame.image.load(f'{BASEDIR}\\assets\\eggs\\bombEgg.png')

    def onEat(self, player):
        player.score -= 5
        player.timeLimit -= 10
        player.stamina = 0
        self.kill()

