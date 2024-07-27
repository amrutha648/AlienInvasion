class Settings:
    def __init__(self):
        # screen settings
        self.screen_width = 800
        self.screen_height = 500
        self.bg_color = (230, 230, 230)

        # ship's speed setting
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

         # alien settings
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1

        self.score_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.1
        # 1 - right, -1 - left
        self.fleet_direction = 1

        self.alien_points = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)