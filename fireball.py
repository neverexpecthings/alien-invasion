import pygame
from pygame.sprite import Sprite


class Fireball(Sprite):
    """La clases para gestionar los poderes."""

    def __init__(self, c_game):
        """Crea un fireball en la posicion de alucard"""
        super().__init__()
        self.screen = c_game.screen
        self.settings = c_game.settings
        self.color = self.settings.fireball_color
        # Creamos el rect del fireball luego lo movemos
        # a la posicion de alucard
        self.rect = pygame.Rect(0, 0, self.settings.fireball_width,
                                self.settings.fireball_height)
        self.rect.midright = c_game.alucard.rect.midright

        # Almacenamos la posicion del fireball como float
        self.x = float(self.rect.x)

    def update(self):
        """Movimiento horizontal del fireball."""
        # Misma logica que el Alien Invasion.
        self.x += self.settings.fireball_speed
        # Actualizamos la posicion del rect
        self.rect.x = self.x

    def draw_fireball(self):
        """Dibujamos el fireball con draw.rect()"""
        pygame.draw.rect(self.screen, self.color, self.rect)
