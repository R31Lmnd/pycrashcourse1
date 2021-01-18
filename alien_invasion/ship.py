import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
# Load ship image and its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
# Start new ships at bottom center of screen
# Store decimal value for more accurate ship positioning on screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    # movement flag
        self.moving_right = False
        self.moving_left = False
# Update position based on movement flag
# Update value, not rect!
    def update(self):
        # Limit ship range to stop it from leaving game window
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
# Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
# Test try it yourself code below (12-2)
# class Purple_alien:
# def __init__(self, ai_game):
        # self.screen = ai_game.screen
        # self.screen_rect = ai_game.screen.get_rect()
        # Load purple alien image and its rect
        # self.image = pygame.image.load('images/try_it_alien.bmp')
        # self.rect = self.image.get_rect()
        # Start new purple alien at center of screen
        # self.rect.center = self.screen_rect.center
# def blitme(self):
# self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
