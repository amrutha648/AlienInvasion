import pygame
from pygame.sprite import Sprite


class Life(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/life.bmp')
        self.rect = self.image.get_rect()
