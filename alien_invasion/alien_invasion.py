import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien


# from ship import Purple_alien


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # To open game in full-screen window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create game stats instance for stats storage
        self.stats =GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        # Create fleet of aliens
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # Determine how many alien rows will fit on screen
        # Create 1st row of aliens in fleet
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        # Create full fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        # Create alien and place it in row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        # Respond appropriately if alien has reached screen edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        # Drop fleet and change direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        # Check if any aliens have touched screen bottom
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Same as ship collision
                self._ship_hit()
                break

    # self.ship = Purple_alien(self)

    def run_game(self):
        while True:
            self._check_events()  # New refactoring method
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()  # New refactoring method

    def _check_events(self):
        # Respond to keypress/mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    # Respond to keydown L/R events

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    # Respond to keyup L/R events

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        # Update position of fired bullets, get rid of bullets that have disappeared off screen.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Remove bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(
        self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Destroy existing bullets, create new fleet
            self.bullets.empty()
            self._create_fleet()

        # For test purposes only: print(len(self.bullets))

    def _update_aliens(self):
        # Update positions of aliens in fleet based on fleet's edge proximity
        self._check_fleet_edges()
        self.aliens.update()
        # Detect alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # Detect aliens touching screen bottom
        self._check_aliens_bottom()


    def _ship_hit(self):
        if self.stats.ships_left > 0:
        # Decrement remaining ships
            self.stats.ships_left -= 1
            # Remove remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            # Create new fleet, center ship
            self._create_fleet()
            self.ship.center_ship()
            # Pause
            sleep(.5)
        else:
            self.stats.game_active = False

    def _update_screen(self):
        # Update images on screen and flip to new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
