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

        # Configuracion de las balas
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 9
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 7

        # Configuracion de los aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction de 1 representa derecha; -1 izquierda.
        self.fleet_direction = 1
