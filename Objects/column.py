# We will create a column object that will be used as an obstacle in the game. 
# The column will have two pipes, one at the top and one at the bottom. 
# The column will move from right to left and will be removed from the game when it goes out of the screen. 
# We will also check if the column is passed by the player.

# Import the necessary libraries.
import pygame.sprite
import assets
import configs
import random
from layer import Layer

# Create a new class called Column that inherits from pygame.sprite.Sprite.
class Column(pygame.sprite.Sprite):
    def __init__(self, *groups):
        """Create a new column."""  
        super().__init__(*groups)
        self._layer = Layer.OBSTACLE
        self.gap = 100
        self.sprite = assets.get_sprites("pipe-green")
        self.sprite_rect = self.sprite.get_rect()
        self.bottom_pipe = self.sprite
        self.bottom_pipe_rect = self.bottom_pipe.get_rect(topleft=(0, self.sprite_rect.height + self.gap))
        self.top_pipe = pygame.transform.flip(self.sprite, False, True)
        self.top_pipe_rect = self.top_pipe.get_rect(topleft=(0, 0))
        self.image = pygame.Surface((self.sprite_rect.width, self.sprite_rect.height * 2 + self.gap), pygame.SRCALPHA)
        self.image.blit(self.bottom_pipe, self.bottom_pipe_rect)
        self.image.blit(self.top_pipe, self.top_pipe_rect)
        sprite_floor_height = assets.get_sprites("floor").get_rect().height
        min_y = 100
        max_y = configs.HEIGHT - sprite_floor_height - 100
        self.rect = self.image.get_rect(midleft=(configs.WIDTH, random.uniform(min_y, max_y)))
        self.mask = pygame.mask.from_surface(self.image)
        self.passed = False
        

    def update(self):
        """Update the column."""
        self.rect.x -= 2
        
        if self.rect.right <= 0:
            self.kill()

    def is_passed(self):
        """Check if the column is passed."""
        if self.rect.x < 50 and not self.passed:
            self.passed = True
            return True
        
        return False