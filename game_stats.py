class GameStats:
    """Trackea las estadisticas del juego."""

    def __init__(self, ai_game):
        """Inicializa las estadisticas."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """Inicializa las estadisticas que pueden cambiar durante el juego."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
