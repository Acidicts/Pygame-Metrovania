import pygame


# Sprite Settings
ANIMATION_SPEED = 1


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, img, groups):
        # noinspection PyTypeChecker
        super().__init__(groups)

        self.game = game
        self.img = img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, screen):
        screen.blit(self.img, self)

    def update(self):
        pass


class AnimatedSprite(Sprite):
    def __init__(self, pos, frames, groups):
        super().__init__(pos, img, groups)

        self.frames, self.frame_index = frames, 0

    def animate(self, dt):
        self.frame_index += ANIMATION_SPEED * dt
        self.img = self.frames[int(self.frame_index) % len(self.frames)]

    def update(self, dt):
        self.animate(dt)
