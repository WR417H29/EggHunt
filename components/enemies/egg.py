import random
import pygame
from utils.consts import WIDTH, HEIGHT, BASEDIR
from components.base.enemy import Enemy

pygame.init()

class Egg(Enemy):
    def __init__(self, spawn, radius, radiusDrawn=False):
        Enemy.__init__(self, spawn, radius, radiusDrawn)
        self.image = pygame.image.load(f'{BASEDIR}\\assets\\eggs\\egg.png')
        self.moveSpeed = 0.75
    
    def __repr__(self):
        return '<Egg %s>' % self.rect

    def onEat(self, player):
        player.score += 1
        player.stamina += 10 if player.stamina < player.staminaLimit else player.staminaLimit - player.stamina
        self.kill()

