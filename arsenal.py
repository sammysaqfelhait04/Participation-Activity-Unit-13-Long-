
from typing import TYPE_CHECKING
import pygame
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class ShipArsenal:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        self.arsenal.update()
        self.remove_offscreen_bullets()

    def remove_offscreen_bullets(self):
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw_arsenal(self):
        for bullet in self.arsenal.sprites():
            bullet.draw_bullet()

    def fire_bullet(self):
        if len(self.arsenal) < self.settings.bullets_allowed:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
    