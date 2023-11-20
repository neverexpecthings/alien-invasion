import pygame
import sys
from settings_c import Settings
from alucard import Alucard
from fireball import Fireball
from sword import Sword
from scorpio import Scorpio


class Castlevania():
    """La clase principal para gestionar las piezas y sus comportamientos."""

    def __init__(self):
        """Inicializamos el juego y creamos sus recursos."""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Castlevania")

        self.alucard = Alucard(self)
        self.fireballs = pygame.sprite.Group()
        self.swords = pygame.sprite.Group()
        self.scorpions = pygame.sprite.Group()

    def run_game(self):
        """Iniciamos el circuito principal."""
        while True:
            self._check_events()
            self.alucard.update()
            self._update_fireballs()
            self._update_swords()
            self._update_scorpions()
            self._update_screen()
            self.clock.tick(75)

    def _check_events(self):
        """Activa escucha de los eventos del mouse y teclado."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respuesta a las teclas oprimidas"""
        if event.key == pygame.K_d:
            self.alucard.moving_right = True
        elif event.key == pygame.K_a:
            self.alucard.moving_left = True
        elif event.key == pygame.K_w:
            self.alucard.moving_up = True
        elif event.key == pygame.K_s:
            self.alucard.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_e:
            self._shoot_fireball()

    def _check_keyup_events(self, event):
        """Respuesta a las teclas soltadas"""
        if event.key == pygame.K_d:
            self.alucard.moving_right = False
        elif event.key == pygame.K_a:
            self.alucard.moving_left = False
        elif event.key == pygame.K_w:
            self.alucard.moving_up = False
        elif event.key == pygame.K_s:
            self.alucard.moving_down = False

    def _shoot_fireball(self):
        """Creamos un fireball y lo agregamos al grupo."""
        if len(self.fireballs) < self.settings.fireballs_allowed:
            new_fireball = Fireball(self)
            self.fireballs.add(new_fireball)

    def _update_fireballs(self):
        """Actualizamos la posicion de los fireballs y eliminamos las que van
        saliendo de la pantalla."""
        self.fireballs.update()

        # Eliminamos las que salen.
        for fireball in self.fireballs.copy():
            if fireball.rect.left > self.settings.screen_width:
                self.fireballs.remove(fireball)

        self._check_fireball_scorpio_collisions()

    def _check_fireball_scorpio_collisions(self):
        """Respuesta a la colision de alien-bala."""
        # Quitamos cualquier fireball y scorpion que hayan colisionado.
        collisions = pygame.sprite.groupcollide(
            self.fireballs, self.scorpions, True, True
        )

        if not self.scorpions:
            # Quitamos balas y hacemos otra scorpio
            self._make_scorpio()

    def _make_sword(self):
        """Creamos una espada y la agregamos al grupo."""
        if len(self.swords) < self.settings.swords_allowed:
            new_sword = Sword(self)
            self.swords.add(new_sword)

    def _update_swords(self):
        """Actualizamos la posicion de las espadas y eliminamos las que van
        saliedo de la pantalla."""
        # Creamos si no hay espadas y esperamos a que se elimine para crear otra.
        self._make_sword()

        # Actualizamos la posicion de las balas
        self.swords.update()

        # Eliminamos las espadas que ya han desaparecido.
        for sword in self.swords.copy():
            if sword.rect.top >= self.settings.screen_height:
                self.swords.remove(sword)

    def _make_scorpio(self):
        """Creamos una espada y la agregamos al grupo."""
        if len(self.scorpions) < self.settings.scorpio_allowed:
            new_scorpio = Scorpio(self)
            self.scorpions.add(new_scorpio)

    def _update_scorpions(self):
        """Actualizamos la posicion de las scorpions y eliminamos las que van
        saliedo de la pantalla."""
        # Creamos si no hay scorpions y esperamos a que se elimine para crear otra.
        self._make_scorpio()

        # Actualizamos la posicion de las balas
        self.scorpions.update()

        # Eliminamos las espadas que ya han desaparecido.
        for scorpio in self.scorpions.copy():
            if scorpio.rect.right < 0:
                self.scorpions.remove(scorpio)

    def _update_screen(self):
        """Rehacemos la pantalla por cada paso del loop."""
        self.screen.fill(self.settings.bg_color)
        for fireball in self.fireballs.sprites():
            fireball.draw_fireball()
        self.alucard.blitme()
        self.swords.draw(self.screen)
        self.scorpions.draw(self.screen)

        # Hacer visible la pantalla mas reciente con flip
        pygame.display.flip()


if __name__ == '__main__':
    # Creamos las instacia del juego y la abrimos.
    c = Castlevania()
    c.run_game()
