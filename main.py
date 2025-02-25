"""
Author: Mosia Marate
Date: 28 January 2025
Pjoject: Flappy Bird
Description: This is a simple game called Flappy Bird. 
             The player has to control a bird and make it pass through the columns without hitting them. 
             The player gets a point for each column passed. 
             The game ends when the bird hits a column."""

# This file is responsible for the game loop and to render the sprites on the screen.

# Import necessary libraries.
import pygame
import assets
import configs

# Import classes.
from Objects.background import Background
from Objects.floor import Floor
from Objects.column import Column
from Objects.bird import Bird
from Objects.start_game import GameStartMessage
from Objects.game_over import GameOverMessage
from Objects.score import Score

# Initialize pygame.
pygame.init()

# Create the screen and clock.
screen = pygame.display.set_mode((configs.WIDTH, configs.HEIGHT))
clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT

# Initialize the variables.
running = True
game_over = False
game_started = False
# score = 0

# Load the sprites.
assets.load_sprites()
assets.load_sounds()
sprites = pygame.sprite.LayeredUpdates()

def sprite_create():
    # Create the objects.
    Background(0, sprites)
    Background(1, sprites)
    Floor(0, sprites)
    Floor(1, sprites)

    return Bird(sprites), GameStartMessage(sprites), Score(sprites)

bird, game_start_message, score = sprite_create()

# Game loop.
while running:
    """Handle the events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == column_create_event:
            Column(sprites)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_started and not game_over:
                game_started = True
                game_start_message.kill()
                pygame.time.set_timer(column_create_event, 1500)

            if event.key == pygame.K_ESCAPE and game_over:
                game_over = False
                game_started = False
                sprites.empty()
                bird, game_start_message, score = sprite_create()

            if event.key == pygame.K_r and game_over:
                game_over = False
                games_tarted = False
                sprites.empty()
                bird, game_start_message, score = sprite_create()
        bird.handle_event(event)

    """Update the sprites."""
    screen.fill(0)
    sprites.draw(screen)

    # Play background music.
    

    """Update the game."""
    if game_started and not game_over:
        sprites.update()

    """Check the collision."""
    if bird.check_collision(sprites) and not game_over:
        game_over = True
        game_started = False
        GameOverMessage(sprites)
        pygame.time.set_timer(column_create_event, 0)
        assets.play_sound("hit")
    

    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed():
            score.value += 1
            assets.play_sound("point")

    # score.value += 1
    # score.value = max(score.value, 0)
    """Render the score."""
    pygame.display.set_caption(f"Flappy Bird - Score: {score}")

    """Flip the display."""
    pygame.display.flip()
    clock.tick(configs.FPS)


# Quit pygame.
pygame.quit()