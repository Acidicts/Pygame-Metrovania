from sprites import Sprite
from settings import *


class Collider:
    def __init__(self, width, height, x, y, points=None):
        self.pos = (x, y)
        self.rect = pygame.Rect(x, y, 0, 0)

        if not points:
            self.rect = pygame.Rect(x, y, width, height)
            self.old_rect = self.rect.copy()

        if points:
            self.image = pygame.Surface((width, height)).convert_alpha()
            pygame.draw.polygon(self.image, (255, 0, 0), points)


class SemiCollider(pygame.sprite.Sprite):
    # noinspection PyTypeChecker
    def __init__(self, width, height, x, y, groups):
        super().__init__(groups)
        self.rect = pygame.Rect(x, y, width, height)
        self.old_rect = self.rect.copy()