import pygame
from pygame.sprite import Sprite
from random import randint


class Scorpio(Sprite):
    """La clase que representa un solo scorpion."""

    def __init__(self, c_game):
        """Inicializa el scorpion y sus atributos."""
        super().__init__()
        self.screen = c_game
        self.settings = c_game.settings

        # Cargamos la imagen y configuramos su rect
        self.image = pygame.image.load("images/Scorpio.png")
        self.rect = self.image.get_rect()

        # Comenzamos cada nuevo scorpion en algun random de la parte inferior
        self.random_number = randint(self.settings.screen_height / 2, 650)
        self.rect.y = self.random_number
        self.rect.x = self.settings.screen_width - self.rect.width

        # Almacenamos la posicion exacta horizontal del scorpion
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Retorna True si el alien esta en el borde."""
        return (self.rect.top <= self.settings.screen_height / 2) or (
            self.rect.bottom >= self.settings.screen_height
        )

    def update(self):
        """Movimiento horizontal de la scorpio."""
        # Actualizamos la posicion del scorpio.
        self.x -= self.settings.scorpio_speed
        self.y += self.settings.scorpio_speed * self.settings.scorpio_direction
        # Le pasamos el valor al rect
        self.rect.x = self.x
        self.rect.y = self.y
