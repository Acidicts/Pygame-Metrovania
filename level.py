from player import Player
from support import *


class Level:
    def __init__(self, level, all_sprites):
        self.level = level
        self.all_sprites = all_sprites

        self.player = Player((200, 350), load_spritesheet('assets/sprites/u.png', 7, 9, 0), self.all_sprites)
