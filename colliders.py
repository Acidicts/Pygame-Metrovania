from sprites import Sprite
from settings import *


class Collider:
    def __init__(self, width, height, x, y):
        self.rect = pygame.Rect(x, y, width, height)
        self.old_rect = self.rect.copy()


class SemiCollider(pygame.sprite.Sprite):
    # noinspection PyTypeChecker
    def __init__(self, width, height, x, y, groups):
        super().__init__(groups)
        self.rect = pygame.Rect(x, y, width, height)
        self.old_rect = self.rect.copy()