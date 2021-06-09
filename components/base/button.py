import pygame

from utils.consts import BASEDIR

pygame.init()

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, text, func=None):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont('arial', 24)
        self.image = pygame.image.load(f'{BASEDIR}\\assets\\buttons\\button_blue.png')
        self.rect = self.image.get_rect()
        self.pos = pos
        self.text = text
        self.func = func
    
    def __repr__(self):
        return '<Button %s>' % self.text

    def draw(self, screen):
        drawn = self.font.render(self.text, True, (0, 0, 0))        

        screen.blit(self.image, self.pos)
        screen.blit(drawn, [self.pos[0], self.pos[1]])
    
    def onClick(self, mouse):
        if self.pos[0] <= mouse[0] <= self.pos[0]+self.rect[2] and self.pos[1] <= mouse[1] <= self.pos[1]+self.rect[3] :
            self.func()            

