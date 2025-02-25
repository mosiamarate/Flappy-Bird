# We will create a class that will be responsible for the score of the game. 
# It will be updated every time the player passes through a column.

# Import the necessary libraries.
import pygame.sprite
import assets
import configs
from layer import Layer

# Create a new class called Score that inherits from pygame.sprite.Sprite.
class Score(pygame.sprite.Sprite):
    def __init__(self, *groups):
        """Create a new score."""
        super().__init__(*groups)
        self._layer = Layer.UI
        self.value = 0
        self.image = pygame.surface.Surface((0, 0), pygame.SRCALPHA)
        self.__create()


    def __create(self):
        """Create the score."""
        self.str_value = str(self.value)

        self.images = []
        self.width = 0

        for str_value_char in self.str_value:
            img = assets.get_sprites(str_value_char)
            self.images.append(img)
            self.width += img.get_width()

        self.height = self.images[0].get_height()
        self.image = pygame.surface.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(configs.WIDTH / 2, 50))

        x = 0
        for img in self.images:
            self.image.blit(img, (x, 0))
            x += img.get_width()

        
    def update(self):
        """Update the score."""
        self.__create()