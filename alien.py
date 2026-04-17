
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Bullet(Sprite):
    def __init__(self, fleet: "AlienFleet", x: float, y: float):
        super().__init__()

        self.fleet = fleet
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_width, self.settings.bullet_height)
        )

        self.rect = self.image.get_rect()
        self.rect.midtop = fleet.game.ship.rect.midtop
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        temp_speed = self.settings.fleet_speed
        self.x+= temp_speed * self.settings.fleet_direction
        self.rect.x = self.x
        self.y += self.settings.fleet_drop_speed
        self.rect.y = self.y

        

        def check_edges(self):
            return self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left

        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed


    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)

        