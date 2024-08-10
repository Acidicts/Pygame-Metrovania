from settings import *


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Metrovania")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        level = open("assets/maps/room1.json")
        self.level = json.load(level)
        self.background = pygame.image.load("assets/maps/room1.png")
        self.background = pygame.transform.scale(self.background, (self.background.get_width() * 4, self.background.get_height() * 4))

        # self.room = Level(self.level, self.screen)

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

            self.screen.blit(self.background, (0, 0))

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()

    pygame.quit()
    sys.exit()
