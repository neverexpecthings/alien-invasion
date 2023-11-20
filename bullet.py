import pygame
from pygame.sprite import Sprite  # Podemos agrupar elementos con este modulo


class Bullet(Sprite):
    """La clase para gestionar las balas que dispara la nave."""

    def __init__(self, ai_game):
        """Crea una bala en la posicion de la nave."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Crea un rect de la bala en la posicion (0, 0) y luego lo mueve a la posicion
        # correspondiente
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Almanenamos la posicion de la bala como Float
        self.y = float(self.rect.y)

    def update(self):
        """Movimiento vertical de la bala."""
        # Misma logica que con la nave, vamos actualizando la posicion de la bala progresivamente
        self.y -= self.settings.bullet_speed
        # Actualizamos la posicion del rect
        self.rect.y = self.y

    def draw_bullet(self):
        """Dibujamos la bala en la pantalla. Para eso usamos draw.rect()"""
        pygame.draw.rect(self.screen, self.color, self.rect)
