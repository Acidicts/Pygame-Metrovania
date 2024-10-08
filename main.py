from settings import *
from level import Level
from player import Player
from groups import AllSprites
from support import load_spritesheet


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Metrovania")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.all_sprites = AllSprites()

        level = open("assets/maps/room1.json")
        self.level = json.load(level)

        self.room = Level(self.level, self.all_sprites)

        for layer in self.level['layers']:
            print(layer['name'])

    def run(self):
        run = True
        dt = self.clock.tick() / 1000

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.screen.fill((0, 0, 0))

            self.all_sprites.update(dt, self.room.player, self.room.colliders)
            self.all_sprites.custom_draw(self.screen)

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()

    pygame.quit()
    sys.exit()
