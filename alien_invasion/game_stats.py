class GameStats:
    # Track stats for Alien Invasion
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        # Start game in active state
        self.game_active = True

    def reset_stats(self):
        # Initialize stats that change during game
        self.ships_left = self.settings.ship_limit