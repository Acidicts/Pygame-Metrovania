import pygame


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def draw(self, screen):
        for sprite in self:
            sprite.draw(screen)

    def update(self, dt):
        for sprite in self.sprites():
            sprite.update(dt)
