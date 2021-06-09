import random
import pygame
from utils.consts import WIDTH, HEIGHT, BASEDIR
from components.enemies.egg import Egg

class StaminaEgg(Egg):
    def __init__(self, spawn, radius, radiusDrawn=False):
        Egg.__init__(self, spawn, radius, radiusDrawn)
        self.image = pygame.image.load(f'{BASEDIR}\\assets\\eggs\\staminaEgg.png')

    def onEat(self, player):
        player.score += 1
        player.staminaLimit += 5
        player.stamina += 10 if player.stamina+10 < player.staminaLimit else player.staminaLimit - player.stamina
        self.kill()
