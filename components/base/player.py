import json
import pygame

from utils.consts import BASEDIR, WIDTH, HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self, spawn):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'{BASEDIR}\\assets\\players\\player.png')
        self.rect = self.image.get_rect()
        self.spawn = spawn
        self.rect.x = self.spawn['x']
        self.rect.y = self.spawn['y']
        self.moveSpeed = 1.5
        

        with open("config.json") as f:
            settings = json.load(f)
        
        self.preLoad = settings['movement']
        self.controls = {
            'up': pygame.key.key_code(self.preLoad['up']),
            'down': pygame.key.key_code(self.preLoad['down']),
            'left': pygame.key.key_code(self.preLoad['left']),
            'right': pygame.key.key_code(self.preLoad['right']),
            'toggleSprint': pygame.key.key_code(self.preLoad['toggleSprint'])
        }
    
    def __repr__(self):
        return '<Player %s>' % self.rect


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def getPos(self):
        return [self.rect.x, self.rect.y]

    def update(self, keys):
        self.rect.y -= (keys[self.controls['up']]) * self.moveSpeed
        self.rect.y += (keys[self.controls['down']]) * self.moveSpeed
        self.rect.x -= (keys[self.controls['left']]) * self.moveSpeed
        self.rect.x += (keys[self.controls['right']]) * self.moveSpeed

        self.rect.left = min(max(0, self.rect.left), WIDTH)
        self.rect.right = min(max(0, self.rect.right), WIDTH)
        self.rect.top = min(max(0, self.rect.top), HEIGHT)
        self.rect.bottom = min(max(0, self.rect.bottom), HEIGHT)

        self.moveSpeed = 1
        if (keys[self.controls['toggleSprint']]) != 0:
            self.moveSpeed = 3
