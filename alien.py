import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """La clase que representa un solo alien en la flota."""

    def __init__(self, ai_game):
        """Inicializa el alien y asignamos su posicion inicial."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Cargamos la imagen del alien y configuramos los atributos de su rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Comenzamos cada nuevo alien cerca de la parte superior izquierda de la
        # pantalla.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Almacenamos la exacta posicion horizontal del alien.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Retorna True si el alien esta en el borde."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Mueve el alien a la derecha o izquierda."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
