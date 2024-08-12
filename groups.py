import pygame
from pygame.math import Vector2


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = Vector2(0, 0)
        self.display = pygame.display.get_surface()

    def draw(self, screen):
        for sprite in self:
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.img, offset_pos)

    def update(self, dt, player):
        self.offset.x = player.rect.centerx - self.display.get_width() // 2
        self.offset.y = player.rect.centery - self.display.get_height() // 2

        for sprite in self.sprites():
            sprite.update(dt)