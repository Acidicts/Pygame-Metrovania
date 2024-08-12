import pygame.draw
from pygame import Vector2

from sprites import AnimatedSprite
from support import scale_list, Timer


class Player(AnimatedSprite):
    def __init__(self, pos, frames, groups, colliders):
        frames = scale_list(frames, (4, 4))
        super().__init__(pos, frames, groups)

        self.direction = Vector2(0, 1)
        self.speed = 200
        self.gravity = 30

        self.player = True

        self.colliders = colliders
        self.rect = self.img.get_rect()
        self.hitbox = self.rect.copy().inflate(-self.rect.width // 2, -self.rect.height // 2)

        self.collide_faces = {'top': False, 'bottom': False, 'left': False, 'right': False}

        self.timers = {
            'jump': Timer(500),
        }

    def collision(self, axis):
        collide = False

        for sprite in self.colliders:
            if sprite.rect.colliderect(self.hitbox):
                if axis == 'x':
                    if self.hitbox.left <= sprite.rect.right and int(self.old_rect.left) >= int(sprite.old_rect.right):
                        self.hitbox.left = sprite.rect.right
                        collide = True

                    if self.hitbox.right >= sprite.rect.left and int(self.old_rect.right) <= int(sprite.old_rect.left):
                        self.hitbox.right = sprite.rect.left
                        collide = True

                if axis == 'y':
                    if self.hitbox.top <= sprite.rect.bottom and int(self.old_rect.top) >= int(sprite.old_rect.bottom):
                        self.hitbox.top = sprite.rect.bottom
                        self.direction.y = 0
                        collide = True

                    if self.hitbox.bottom >= sprite.rect.top and int(self.old_rect.bottom) <= int(sprite.old_rect.top):
                        self.hitbox.bottom = sprite.rect.top
                        collide = True
        return collide

    def get_collide_faces(self):
        self.collide_faces = {'top': False, 'bottom': False, 'left': False, 'right': False}
        colliders = {'top': pygame.Rect(self.hitbox.left, self.hitbox.top - 1, self.hitbox.width, 2),
                     'bottom': pygame.Rect(self.hitbox.left, self.hitbox.bottom, self.hitbox.width, 2),
                     'left': pygame.Rect(self.hitbox.left - 1, self.hitbox.top, 2, self.hitbox.height),
                     'right': pygame.Rect(self.hitbox.right, self.hitbox.top, 2, self.hitbox.height)
                     }

        for index, collider in enumerate(colliders.values()):
            if collider.collidelist(self.colliders) > 0:
                self.collide_faces[list(colliders.keys())[index]] = True

    def input(self, dt):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])

        if keys[pygame.K_SPACE] and self.collide_faces['bottom']:
            self.hitbox.y -= 5
            self.direction.y = -27
            self.timers['jump'].activate()

        if not self.collide_faces['bottom']:
            self.direction.y += self.gravity * dt
        elif self.collide_faces['bottom']:
            self.direction.y = min(3, self.direction.y)

    def update(self, dt):
        self.animate(dt)
        win = pygame.display.get_surface()

        pygame.draw.rect(win, self.gravity, self.hitbox, 1)
        pygame.draw.rect(win, (0, 255, 0), self.rect, 1)

        self.input(dt)
        self.get_collide_faces()

        self.rect.midbottom = self.hitbox.midbottom

        self.hitbox.x += self.direction.x * dt * self.speed
        self.collision('x')

        self.hitbox.y += self.direction.y
        self.collision('y')

        for timer in self.timers.values():
            timer.update()

        for collider in self.colliders:
            pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), collider.rect, 2)

        self.old_rect = self.hitbox.copy()
