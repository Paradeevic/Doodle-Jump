from scripts.functions import load_image
from scripts.sprite import Sprite


class Game():
    def __init__(self) -> None:
        self.background_image = load_image('assets','images', 'background.png')
        self.player = Sprite((200, 200), load_image('assets', 'images', 'player.png'))

    def render(self, surface):
        surface.blit(self.background_image, (0, 0))
        self.player.render(surface)
