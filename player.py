import pygame.draw
from pygame import Vector2

from sprites import AnimatedSprite
from support import scale_list


class Player(AnimatedSprite):
    def __init__(self, pos, frames, groups, colliders):
        frames = scale_list(frames, (4, 4))
        super().__init__(pos, frames, groups)

        self.direction = Vector2(0, 1)
        self.speed = 200
        self.gravity = 200

        self.colliders = colliders
        self.hitbox = self.rect

    def collision(self, axis):
        for sprite in self.colliders:
            if sprite.rect.colliderect(self.hitbox):
                if axis == 'x':
                    if self.hitbox.left <= sprite.rect.right and int(self.old_rect.left) >= int(sprite.old_rect.right):
                        self.hitbox.left = sprite.rect.right

                    if self.hitbox.right >= sprite.rect.left and int(self.old_rect.right) <= int(sprite.old_rect.left):
                        self.hitbox.right = sprite.rect.left

                if axis == 'y':
                    if self.hitbox.top <= sprite.rect.bottom and int(self.old_rect.top) >= int(sprite.old_rect.bottom):
                        self.hitbox.top = sprite.rect.bottom
                        if hasattr(sprite, 'moving'):
                            self.rect.top += 6

                    if self.hitbox.bottom >= sprite.rect.top and int(self.old_rect.bottom) <= int(sprite.old_rect.top):
                        self.hitbox.bottom = sprite.rect.top

                    self.direction.y = 0


    def input(self):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])

    def update(self, dt):
        self.animate(dt)

        self.input()

        self.hitbox.y += self.direction.y * dt * self.gravity
        self.collision('y')

        self.hitbox.x += self.direction.x * dt * self.speed
        self.collision('x')

        self.rect = self.hitbox

        for collider in self.colliders:
            pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), collider.rect, 2)

        self.old_rect = self.rect.copy()
