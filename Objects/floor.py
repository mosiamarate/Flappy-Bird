# We will create a floor object that will be used to create the floor of the game.
# Import the necessary libraries.
import pygame.sprite
import assets
import configs
from layer import Layer

# Create a new class called Floor that inherits from pygame.sprite.Sprite.
class Floor(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        """Create a new floor."""
        self._layer = Layer.FLOOR
        self.image = assets.get_sprites("floor")
        self.rect = self.image.get_rect(topleft=(configs.WIDTH * index, configs.HEIGHT - self.image.get_height()))
        self.mask = pygame.mask.from_surface(self.image)
        super().__init__(*groups)
        
    def update(self):
        """Update the floor."""
        self.rect.x -= 2
        
        if self.rect.right <= 0:
            self.rect.x = configs.WIDTH