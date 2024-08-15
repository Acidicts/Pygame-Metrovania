import pygame
from pygame.math import Vector2
from settings import *


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = Vector2(0, 0)
        self.display = pygame.display.get_surface()

        self.background = pygame.image.load("assets/maps/room1.png")
        self.background = pygame.transform.scale(self.background, (self.background.get_width() * SCALE,
                                                                   self.background.get_height() * SCALE))

    def custom_draw(self, screen):
        self.display.blit(self.background, -self.offset)

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset

            self.display.blit(sprite.img, offset_pos)

    def update(self, dt, player, colliders):
        self.offset.x = player.rect.centerx - self.display.get_width() // 2
        self.offset.y = player.rect.centery - self.display.get_height() // 2

        if self.offset.x < 0:
            self.offset.x = 0
        elif self.offset.x > self.background.get_width() - self.display.get_width():
            self.offset.x = self.background.get_width() - self.display.get_width()

        if self.offset.y < 0:
            self.offset.y = 0
        elif self.offset.y > self.background.get_height() - self.display.get_height():
            self.offset.y = self.background.get_height() - self.display.get_height()

        for sprite in self.sprites():
            sprite.update(dt)

        for collider in colliders:
            offset_rect = (collider.rect.topleft - self.offset, (collider.rect.width, collider.rect.height))
            pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), offset_rect, 2)
