import pygame


def load_spritesheet(path, rows, cols, row):
    spritesheet = pygame.image.load(path).convert_alpha()

    y = int(spritesheet.get_width() // rows)
    x = int(spritesheet.get_height() // cols)

    sprites = []

    for i in range(rows):
        sprite = pygame.Surface((x, y))
        sprite.blit(spritesheet, (-i * x, y * row))
        sprite.convert_alpha()
        sprite.set_colorkey((0, 0, 0))
        sprites.append(sprite)

    return sprites


def scale_list(list, scale):
    scale = (scale[0] * list[0].get_width(), scale[1] * list[0].get_height())

    for index, img in enumerate(list):
        list[index] = pygame.transform.scale(img, scale)

    return list
