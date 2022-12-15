
class Settings:
    def __init__(self):
        self.bg_color = (0, 0, 0)
        self.screen_width = 1200
        self.screen_height = 800
        self.ship_limit = 3
        self.bullet_width = 4
        self.bullet_height = 8
        self.bullet_color = (255,20,20)
        self.bullets_allowed = 3
        self.fleet_drop_speed = 15

        #Velocity on wich the game speeds up
        self.speedup_scale = 1.1
        #The speed that points increase
        self.score_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initializes the settings that change during the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 2

        #fleet_direction of 1 represents RIGHT; -1 represents LEFT.
        self.fleet_direction = 0.2
        #Punctuation
        self.alien_points = 50

    def increase_speed(self):
        """increases speed-settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


