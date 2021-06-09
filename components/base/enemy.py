import pygame
import random

from utils.consts import BASEDIR, WIDTH, HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self, spawn, radius, radiusDrawn):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f"{BASEDIR}\\assets\\enemies\\enemy.png")
        self.rect = self.image.get_rect()
        self.spawn = spawn
        self.radius = radius
        self.radiusDrawn = radiusDrawn
        self.rect.x = self.spawn['x']
        self.rect.y = self.spawn['y']

        self.direction = 0

        # up = 0, 
        # left = 1,
        # down = 2,
        # right = 3

    def __repr__(self):
        return '<Enemy %s>' % self.rect

    def draw(self, screen):
        if self.radiusDrawn: pygame.draw.circle(screen, (0, 0, 0), (self.rect[0] + self.rect[2] // 2, self.rect[1] + self.rect[3] // 2), self.radius, 1)

        screen.blit(self.image, self.rect)

    def checkRadius(self, player):
        playerPos = player.getPos() # [x, y]

        self.rect.left = min(max(0, self.rect.left), WIDTH)
        self.rect.right = min(max(0, self.rect.right), WIDTH)
        self.rect.top = min(max(0, self.rect.top), HEIGHT)
        self.rect.bottom = min(max(0, self.rect.bottom), HEIGHT)

        range = [
            [self.rect.x + self.radius,
            self.rect.x - self.radius],
            [self.rect.y + self.radius,
            self.rect.y - self.radius]
        ]

        if playerPos[0] <= range[0][0] and playerPos[0] >= range[0][1] and playerPos[1] <= range[1][0] and playerPos[1] >= range[1][1]:
            diff = [
                playerPos[0] - self.rect.x, 
                playerPos[1] - self.rect.y
            ]

            self.rect.x += 1 if diff[0] >= 1 else -1
            self.rect.y += 1 if diff[1] >= 1 else -1

        else:
            movement = random.randint(0, 90)

            if movement <= 60: # forward
                self.rect.y += -1 if self.direction == 0 else (1 if self.direction == 2 else 0)
                self.rect.x += -1 if self.direction == 1 else (1 if self.direction == 3 else 0)
        
            elif movement > 70 and movement <= 75: # left -> up -> right -> down
                self.rect.y += -1 if self.direction == 1 else (1 if self.direction == 3 else 0)
                self.rect.x += -1 if self.direction == 2 else (1 if self.direction == 0 else 0)

                if self.direction == 0: self.direction = 3
                elif self.direction == 1: self.direction = 0
                elif self.direction == 2: self.direction = 1
                elif self.direction == 3: self.direction = 2

            elif movement > 75 and movement <= 80: # left -> down -> right -> up
                self.rect.y += 1 if self.direction == 3 else (-1 if self.direction == 1 else 0)
                self.rect.x += 1 if self.direction == 0 else (-1 if self.direction == 2 else 0)

                if self.direction == 0: self.direction = 1
                elif self.direction == 1: self.direction = 2
                elif self.direction == 2: self.direction = 3
                elif self.direction == 3: self.direction = 0

            else:
                self.rect.y += 1 if self.direction == 0 else (-1 if self.direction == 2 else 0)
                self.rect.x += 1 if self.direction == 1 else (-1 if self.direction == 3 else 0)

                self.direction = 0 if self.direction == 2 else (2 if self.direction == 0 else self.direction)
                self.direction = 1 if self.direction == 3 else (3 if self.direction == 1 else self.direction)
