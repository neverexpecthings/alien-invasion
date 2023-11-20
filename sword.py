import pygame
from pygame.sprite import Sprite
from random import randint


class Sword(Sprite):
    """La clase que representa una sola espada."""

    def __init__(self, c_game):
        """Inicializa la espada y la posicion inicial."""
        super().__init__()
        self.screen = c_game
        self.settings = c_game.settings

        # Cargamos la imagen de la espada y configuramos los atributos de su rect.
        self.image = pygame.image.load('images/sword_1.bmp')
        self.rect = self.image.get_rect()

        # Comenzamos cada nuevo alien en lugar random de la parte superior
        self.random_number = randint(1, (self.settings.screen_width - 1))
        self.rect.x = self.random_number
        self.rect.y = self.rect.height

        # Almacenamos la exacta posicion vertical de la espada.
        self.y = float(self.rect.y)

    def update(self):
        """Movimiento vertical de la espada."""
        # Actualizamos la posicion de la nave.
        self.y += self.settings.sword_speed
        # Le pasamos el valor al rect
        self.rect.y = self.y
