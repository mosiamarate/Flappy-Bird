# Description: This file contains the code to load all the assets (sprites and sounds) used in the game.

# Import necessary libraries.
import os
import pygame

# Dictionary to store all sprites
sprites = {}
audios = {}  # Dictionary to store all audio

# Load all sprites from the assets folder
def load_sprites():
    """Load all sprites from the assets folder."""
    path = os.path.join("assets", "sprites")  
    for file in os.listdir(path):
        sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))
    
    # return sprites

def get_sprites(name):
    """Return the sprite with the given name."""
    return sprites[name]

def load_sounds():
    """Load all sounds from the assets folder."""
    path = os.path.join("assets", "audios")  
    for file in os.listdir(path):
        audios[file.split('.')[0]] = pygame.mixer.Sound(os.path.join(path, file))

def play_sound(name):
    """Play the sound with the given name."""
    audios[name].play()
    