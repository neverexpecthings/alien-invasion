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
        self.fireball_width = 18
        self.fireball_height = 35
        self.fireball_color = (160, 60, 60)
        self.fireballs_allowed = 5

        # Configuracion de las espadas
        self.sword_speed = 3.5
        self.swords_allowed = 3

        # Configuracion del scorpio
        self.scorpio_speed = 2.5
        self.scorpio_allowed = 3
