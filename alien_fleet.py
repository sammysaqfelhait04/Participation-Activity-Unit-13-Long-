import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from alien import AlienFleet


class AlienFleet:

    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed


        self.create_fleet()

def create_fleet(self) -> None:
    alien_w = self.settings.alien_w
    aline_h = self.settings.alien_h
    screen_w = self.settings.screen_w
    screen_h = self.settings.screen_h

    fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, aline_h)
    half_screen = self.settings.screen_w // 2
    fleet_horizontal_space = fleet_w * alien_w
    fleet_vertical_space = fleet_h * aline_h
    x_offset = int((screen_w - fleet_horizontal_space) // 2)
    y_offset = int(half_screen - fleet_vertical_space // 2)
    self._create_rectangle_fleet(fleet_w, fleet_h, alien_w, aline_h, x_offset, y_offset)

def _create_rectangle_fleet(self, fleet_w: int, fleet_h: int, alien_w: int, aline_h: int, x_offset: int, y_offset: int) -> None:
    for row in range(fleet_h):
        for col in range(fleet_w):
            current_x = x_offset + col * alien_w
            current_y = y_offset + row * aline_h
            if col % 2 == 0 or row % 2 == 0:
                continue
            self._create_alien(current_x, current_y)

    def calculate_fleet_size(self, alien_w: int, screen_w: int, alien_h: int) -> int:
        fleet_w = (screen_w // alien_w)
        screen_h = self.settings.screen_h
        fleet_h = (screen_h // alien_h) // 2

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        return int(fleet_w), int(fleet_h)


    

    def _create_alien(self, current_x, current_y) -> None:
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)

def update_fleet(self) -> None:
    self.check_fleet_edges()
    self.fleet.update()

def check_fleet_edges(self) -> None:
    for alien in self.fleet.sprites():
        if alien.check_edges():
            self.drop_aline_fleet()

            self._change_fleet_direction()
            self.fleet_direction *= -1
            alien.y += self.fleet_drop_speed
            alien.rect.y = alien.y
            break

def _reset_level(self) -> None:
    self.ship.arsenal.empty()
    self.alien_fleet.fleet.empty()
    self.alien_fleet.create_fleet()


def _drop_aline_fleet(self) -> None:
    for alien in self.fleet.sprites():
        print('here we go')
        alien.y += self.fleet_drop_speed
        alien.rect.y = alien.y



def draw_fleet(self) -> None:
    alien: 'Alien'
    for alien in self.fleet:
        alien.draw_alien()



   def check_collisions(self, other_group, ship) -> None:
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)  


def check_fleet_bottom(self) -> bool:
    aline: 'Alien'
    for aline in self.fleet:
        if aline.rect.bottom >= self.game.screen.get_rect().bottom:
            return True
    return False
