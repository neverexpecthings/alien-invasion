from typing import Counter
import pygame
import sys
from time import sleep
from settings_c import Settings
from game_stats_c import GameStats
from alucard import Alucard
from fireball import Fireball
from sword import Sword
from scorpio import Scorpio
from button import Button


class Castlevania:
    """La clase principal para gestionar las piezas y sus comportamientos."""

    def __init__(self):
        """Inicializamos el juego y creamos sus recursos."""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Castlevania")

        # Creamos la instancia para almacenar las estadisticas
        self.stats = GameStats(self)

        self.alucard = Alucard(self)
        self.fireballs = pygame.sprite.Group()
        self.swords = pygame.sprite.Group()
        self.scorpions = pygame.sprite.Group()

        # Empezamos el juego en un estado inactivo
        self.game_active = False

        # Button de Play
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Iniciamos el circuito principal."""
        while True:
            self._check_events()

            if self.game_active:
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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
        elif event.key == pygame.K_p:
            self._start_game()

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

    def _check_play_button(self, mouse_pos):
        """Comienza un nuevo juego cuando le dan click al boton de Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()

    def _start_game(self):
        """Comienza una partida nueva."""
        # Reset the game statistics
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.game_active = True

        # Limpiamos los aliens y balas restantes
        self.scorpions.empty()
        self.swords.empty()
        self.fireballs.empty()

        # Creamos una nueva flota y centramos la nave
        self.alucard.center_alucard()

        # Escondemos el mouse mientras se juega
        pygame.mouse.set_visible(False)

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
        count_scorpions = 0

        if not self.scorpions:
            # Quitamos balas y hacemos otra scorpio y incrementamos el counter
            self._make_scorpio()
            count_scorpions += 1

        if count_scorpions > 3:
            self.settings.increase_speed()
            count_scorpions = 0

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

        # Chequea colisiones de sword-alucard
        if pygame.sprite.spritecollideany(self.alucard, self.swords):
            self._alucard_hit()

        # Eliminamos las espadas que ya han desaparecido.
        for sword in self.swords.copy():
            if sword.rect.top >= self.settings.screen_height:
                self.swords.remove(sword)

    def _alucard_hit(self):
        """Respuesta a alucard siendo hiteado por una espada."""
        # Reducimos las vidas
        self.stats.alucard_left -= 1

        # Eliminamos cualquier espada o scorpion o fireball
        self.fireballs.empty()
        self.scorpions.empty()
        self.swords.empty()

        # Creamos un scorpio, una espada y centramos a alucard
        self._make_scorpio()
        self._make_sword()
        self.alucard.center_alucard()

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
        self._check_scorpions_edges()
        self.scorpions.update()

        # Chequea colisiones de scorpion-alucard
        if pygame.sprite.spritecollideany(self.alucard, self.scorpions):
            self._alucard_hit()

        # Chequeamos si un scorpion llego a la izquierda
        self._check_scorpions_left()

        # Eliminamos las espadas que ya han desaparecido.
        for scorpio in self.scorpions.copy():
            if scorpio.rect.right < 0:
                self.scorpions.remove(scorpio)

        # TODO: Make every scorpion movement independent

    def _check_scorpions_edges(self):
        """Respuesta a un scorpion llega al borde"""
        for scorpion in self.scorpions.sprites():
            if scorpion.check_edges():
                self._change_scorpion_direction()
                break

    def _change_scorpion_direction(self):
        """Cambia de direccion al scorpio"""
        self.settings.scorpio_direction *= -1

    def _check_scorpions_left(self):
        """Chequeamos si un scorpion llega a la izquierda."""
        for scorpio in self.scorpions.sprites():
            if scorpio.rect.right <= 0:
                # Tratamos igual que al ser hiteado
                self._alucard_hit()
                break

    def _update_screen(self):
        """Rehacemos la pantalla por cada paso del loop."""
        self.screen.fill(self.settings.bg_color)
        for fireball in self.fireballs.sprites():
            fireball.draw_fireball()
        self.alucard.blitme()
        self.swords.draw(self.screen)
        self.scorpions.draw(self.screen)

        # Colocamos el boton de Play si el juego esta inactivo
        if not self.game_active:
            self.play_button.draw_button()

        # Hacer visible la pantalla mas reciente con flip
        pygame.display.flip()


if __name__ == "__main__":
    # Creamos las instacia del juego y la abrimos.
    c = Castlevania()
    c.run_game()
