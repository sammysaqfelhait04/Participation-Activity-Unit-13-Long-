import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet

class AlienInvasion:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.running = True
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.bg_image = pygame.image.load(self.settings.bg_file)
        self.bg_image = pygame.transform.scale(
            self.bg_image,
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound_file)
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.7)

        self.clock = pygame.time.Clock()
        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()
        self.arsenal = Arsenal(self)

    def run_game(self):
        while self.running:
            self._check_events()
            self._update_screen(
            )
            self.ship.update()
            self_alien_fleet.update()
            self.clock.tick(self.settings.FpS)





            def _check_collisions(self):
                if self.ship.check_collisions(self.alien_fleet):
                  self._reset_level()

                if self.aline_fleet.check_fleet_bottom():
                    self._reset_level()

                  collisions = self.alien_fleet.check_bullet_collisions(self.ship.arsenal.arsenal, self.ship)
                    if collisions:
                      self.impact_sound.play()
                      self.impact_sound.fadeout(500)

                      
                      


            def _reset_level(self):
                self.arsenal.empty()
                self.alien_fleet.empty()
                self.alien_fleet.create_fleet()
                self.ship.rect.midbottom = self.screen.get_rect().midbottom
                

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_SPACE:
            self.ship.fire()
            self.laser_sound.play()
            self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        self.screen.blit(self.bg_image, (0, 0))
        self.ship.draw()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()