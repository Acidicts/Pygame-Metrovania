import pygame


# Sprite Settings
ANIMATION_SPEED = 0.5


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, img, groups):
        # noinspection PyTypeChecker
        super().__init__(groups)

        self.img = img
        self.rect = self.img.get_rect()
        self.rect.center = pos

    def draw(self, screen):
        screen.blit(self.img, self.rect)

    def update(self, dt):
        pass


class AnimatedSprite(Sprite):
    def __init__(self, pos, frames, groups):
        super().__init__(pos, frames[0], groups)

        self.frames, self.frame_index = frames, 0

    def animate(self, dt):
        self.frame_index += ANIMATION_SPEED * dt
        self.img = self.frames[int(self.frame_index) % len(self.frames)]

    def update(self, dt):
        self.animate(dt)
