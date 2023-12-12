import pygame


class Ship:
    """La clase para gestionar la nave."""

    def __init__(self, ai_image):
        """Inicializamos la nave y configuramos su posicion inicial."""
        self.screen = ai_image.screen
        self.settings = ai_image.settings
        self.screen_rect = ai_image.screen.get_rect()

        # Cargamos la imagen de la nave y conseguimos su rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Colocamos cada nueva nave en la parte central de abajo de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

        # Almacenamos un float para la posicion de la nave
        self.x = float(self.rect.x)

        # Flag de movimiento; comienza con la nave estatica
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualizamos la posicion de la nave basado en el flag de movimiento."""
        # Actualizamos el valor x de la nave, no su rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Actualizamos entonces el objecto, ya que, rect no toma float value
        self.rect.x = self.x

    def center_ship(self):
        """Centra la nave en la pantalla."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Dibujamos la nave en su posicion actual."""
        self.screen.blit(self.image, self.rect)
