import pygame
from utils.consts import WIDTH, HEIGHT
from components.base.player import Player

class PlayerWS(Player):
    def __init__(self, spawn, timeLimit):
        Player.__init__(self, spawn)
        self.sprinting = False
        self.stamina = 100
        self.staminaLimit = 100
        self.timeLimit = timeLimit
        self.score = 0
    
    def update(self, keys):
        if self.stamina <= 1:
            self.sprinting = False
        if self.sprinting and self.stamina > 0:
            self.moveSpeed = 3
            self.stamina -= 1
        else:
            self.moveSpeed = 1
            self.stamina += self.staminaLimit / 150 if self.stamina < self.staminaLimit else 0

        self.rect.y -= (keys[self.controls['up']]) * self.moveSpeed
        self.rect.y += (keys[self.controls['down']]) * self.moveSpeed
        self.rect.x -= (keys[self.controls['left']]) * self.moveSpeed
        self.rect.x += (keys[self.controls['right']]) * self.moveSpeed

        self.rect.left = min(max(0, self.rect.left), WIDTH)
        self.rect.right = min(max(0, self.rect.right), WIDTH)
        self.rect.top = min(max(0, self.rect.top), HEIGHT)
        self.rect.bottom = min(max(0, self.rect.bottom), HEIGHT)

