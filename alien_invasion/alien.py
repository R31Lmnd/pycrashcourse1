import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load alien image, set rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # Start new alien in top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store alien's horiz. position
        self.x = float(self.rect.x)

    # From PyGame Documentation """method to control sprite behavior
        # Sprite.update(*args, **kwargs):
        # The default implementation of this method does nothing; it's just a convenient "hook"
        # that you can override. This method is called by Group.update() with whatever
        # arguments you give it. There is no need to use this method if not using
        # the convenience method by the same name in the Group class."""
    # https://www.pygame.org/docs/ref/sprite.html

    def update(self):
        pygame.sprite.Sprite.update(self)
        self.x += (self.settings.alien_speed *
                    self.settings.fleet_direction)
        self.rect.x = self.x


    def check_edges(self):
        # Return True if alien is at screen edge
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True



