import pygame


class Alucard():
    """Clase para personaje Alucard."""

    def __init__(self, c_image):
        """Inicializamos a Alucard y su posicion inicial."""
        self.screen = c_image.screen
        self.setting = c_image.settings
        self.screen_rect = c_image.screen.get_rect()

        # Cargamos la imagen y sus rect.
        self.image = pygame.image.load('images/alucard.bmp')
        self.rect = self.image.get_rect()

        # Colocamos cada nueva alucard en el primer tercio de abajo hacia arriba de la pantalla.
        self.rect.center = self.screen_rect.center

        # Almacenamos un float para para la posicion de la nave
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Flag del movimiento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Movemos a Alucard basado en el flag de movimiento"""
        # Cambiamos x, no su rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.alucard_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.alucard_speed
        # Cambiamos y, no su rect
        if self.moving_up and self.rect.top > 0:
            self.y -= self.setting.alucard_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.alucard_speed

        # Actualizamos entonces el objecto, ya que, rect no toma float value
        self.rect.x = self.x
        self.rect.y = self.y

    def center_alucard(self):
        "Centra a alucard"
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Dibujamos la imagen en su posicion actual"""
        self.screen.blit(self.image, self.rect)
