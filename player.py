from sprites import AnimatedSprite
from support import scale_list


class Player(AnimatedSprite):
    def __init__(self, pos, frames, groups):
        frames = scale_list(frames, (4, 4))
        super().__init__(pos, frames, groups)
