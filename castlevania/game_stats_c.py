class GameStats:
    """Trackeamos las estadisticas para Castlevasnia."""

    def __init__(self, c_game):
        """Inicializamos estadisticas."""
        self.settings = c_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Inicializamos las estadisticas que pueden cambiar durante el juego."""
        self.alucard_left = self.settings.alucard_limit
