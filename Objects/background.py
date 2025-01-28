# Import necessary libraries.
import pygame.sprite
import assets
import configs
from layer import Layer

# Create a new class called Background that inherits from pygame.sprite.Sprite.
class Background(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        """Create a new background."""
        super().__init__(*groups)
        self._layer = Layer.BACKGROUND
        self.image = assets.get_sprites("background")
        self.rect = self.image.get_rect(topleft=(configs.WIDTH * index, 0))

    def update(self):
        """Update the background."""
        self.rect.x -= 2

        if self.rect.right <= 0:
            self.rect.x = configs.WIDTH