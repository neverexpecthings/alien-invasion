import pygame.font


class Button:
    """Una clase para construir botones para el juego."""

    def __init__(self, ai_game, msg):
        """Inicializamos los atributos de los botones."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Configuramos las dimensiones y propiedades del boton.
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Contruimos el rect del boton y los centramos.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # El mensaje del botón sólo debe prepararse una vez.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Transforma el msg en una imagen renderizada y centra el texto dentro del boton."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Dibuja un boton en blanco y luego coloca el mensaje."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
