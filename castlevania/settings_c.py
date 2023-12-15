class Settings:
    """Una clase para almacenar todas las configuraciones del juego."""

    def __init__(self):
        """Inicializamos las configuraciones del juego."""
        # Configuracion de la pantalla.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (20, 12, 24)

        # Configuracion de Alucard
        self.alucard_speed = 5.5
        self.alucard_limit = 3

        # Configuracion de los fireballs
        self.fireball_speed = 7.5
        self.fireball_width = 9
        self.fireball_height = 17.5
        self.fireball_color = (160, 60, 60)
        self.fireballs_allowed = 4

        # Configuracion de las espadas
        self.sword_speed = 3.5
        self.swords_allowed = 2

        # Configuracion del scorpio
        self.scorpio_speed = 2.5
        self.scorpio_allowed = 2
        self.scorpio_direction = 1

        # Rapidez del juego
        self.speedup_scale = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializamos las configuraciones que cambiaran durante el juego."""
        self.alucard_speed = 4
        self.fireball_speed = 6
        self.scorpio_speed = 1
        self.sword_speed = 2

        # scorpio_direction en 1 representa abajo, -1 arriba
        self.scorpio_direction = 1

    def increase_speed(self):
        """Incrementamos la velocidad."""
        self.alucard_speed *= self.speedup_scale
        self.scorpio_speed *= self.speedup_scale
        self.sword_speed *= self.speedup_scale
        self.fireball_speed *= self.speedup_scale
