# We will create a new class called Game
# OverMessage that inherits from pygame.sprite.Sprite.
# This class will display a message on the screen when the game is over.

# Import necessary libraries.
import pygame.sprite
import assets, configs
from layer import Layer

# Create a new class called GameStartMessage that inherits from pygame.sprite.Sprite.
class GameOverMessage(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self._layer = Layer.UI
        self.image = assets.get_sprites("gameover")
        self.rect = self.image.get_rect(center=(configs.WIDTH / 2, configs.HEIGHT / 2))