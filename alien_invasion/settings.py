class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # self.bg_color = (64, 224, 255)
        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        # TEST: self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (51, 255, 51)
        self.bullets_allowed = 3
        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # TEST: self.fleet_drop_speed = 100
        # fleet direction of 1 repr. Right, -1 repr. Left
        self.fleet_direction = 1



