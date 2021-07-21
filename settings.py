class Settings:
    """A class to store game settings"""

    def __init__(self):
        """Initialise game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5