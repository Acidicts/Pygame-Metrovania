from player import Player
from support import *
from settings import *
from colliders import Collider, SemiCollider


class Level:
    def __init__(self, level, all_sprites):
        self.level = level
        self.all_sprites = all_sprites

        self.platforms = pygame.sprite.Group()
        self.colliders = self.setup()

        self.player = Player((500, 500), load_spritesheet('assets/sprites/u.png', 8, 9, 0), self.all_sprites,
                             self.colliders)

    def setup(self):

        colliders = []
        for layer in self.level['layers']:
            if layer['name'] == 'colliders':
                for collider in layer['objects']:
                    if not collider['type'] == 'passthrough':
                        colliders.append(Collider(collider['width'] * SCALE,
                                                  collider['height'] * SCALE,
                                                  collider['x'] * SCALE,
                                                  collider['y'] * SCALE
                                                  ))
                    else:
                        colliders.append(SemiCollider(collider['width'] * SCALE,
                                                      collider['height'] * SCALE,
                                                      collider['x'] * SCALE,
                                                      collider['y'] * SCALE,
                                                      self.platforms
                                                      ))

        return colliders
