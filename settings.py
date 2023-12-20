class Settings:
    """Una clase para almacenar todas las configuraciones del juego."""

    def __init__(self):
        """Inicializamos las configuraciones del juego."""
        # Configuracion de la pantalla.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configuracion de la nave
        self.ship_speed = 2.5
        self.ship_limit = 3

        # Configuracion de las balas
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 9
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 7

        # Configuracion de los aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 50
        # fleet_direction de 1 representa derecha; -1 izquierda.
        self.fleet_direction = 1

        # Rapidez del juego
        self.speedup_scale = 1.1

        # Rapidez del incremento de puntos.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializamos las configuraciones que cambiara durante el juego."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # fleet_direction en 1 representa derecha, -1 izquierda
        self.fleet_direction = 1

        # Configuraciones del scoring.
        self.alien_points = 50

    def increase_speed(self):
        """Incrementamos la velocidad y el valor de los puntos."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
