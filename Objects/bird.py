# This file contains the Bird class that represents the bird in the game.

# Import the necessary libraries. 
import pygame.sprite
import assets
import configs
from layer import Layer
from Objects.column import Column
from Objects.floor import Floor

# Create a new class called Bird that inherits from pygame.sprite.Sprite.
class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups):
        """Create a new bird."""
        super().__init__(*groups)
        self._layer = Layer.PLAYER
        self.images = [
            assets.get_sprites("redbird-upflap"), 
            assets.get_sprites("redbird-midflap"), 
            assets.get_sprites("redbird-downflap")
            ]
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(-50, 50))
        self.mask = pygame.mask.from_surface(self.image)
        self.flap = 0

    def update(self):
        """Update the bird."""
        self.images.insert(0, self.images.pop())
        self.image = self.images[0]

        self.flap += configs.GRAVITY
        self.rect.y += self.flap

        if self.rect.x < 50:
            self.rect.x += 3

    def handle_event(self, event):
        """Handle the events."""
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.flap = 0
            self.flap -= 6
            assets.play_sound("wing")
    
    def increase_bird_speed(self, score):
        """Increase the bird's speed based on the score."""
        if score % 10 == 0:
            configs.GRAVITY += 0.5


    def check_collision(self, sprites):
        """Check the collision between the bird and the sprite."""
        for sprite in sprites:
            if ((type(sprite) is Column or type(sprite) is Floor) and sprite.mask.overlap(
                self.mask, (self.rect.x - sprite.rect.x, self.rect.y - sprite.rect.y)) or 
                self.rect.bottom < 0):
                return True
        
        return False
