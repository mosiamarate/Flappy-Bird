# We will create a new class called GameStartMessage that inherits from pygame.sprite.Sprite. 
# This class will display a message on the screen when the game starts

# Import necessary libraries.
import pygame.sprite
import assets, configs
from layer import Layer

# Create a new class called GameStartMessage that inherits from pygame.sprite.Sprite.
class GameStartMessage(pygame.sprite.Sprite):
    "Create a new game start message."
    def __init__(self, *groups):
        super().__init__(*groups)
        self._layer = Layer.UI
        self.image = assets.get_sprites("message")
        self.rect = self.image.get_rect(center=(configs.WIDTH / 2, configs.HEIGHT / 2))
    
