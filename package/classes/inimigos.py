import pygame
from pygame.locals import *
from package.classes.nave import Nave
from package.classes.laser import Laser

#img das naves
INIMIGO_VERMELHO = pygame.image.load("package/assets/images/inimigo_vermelho.png")
INIMIGO_VERDE = pygame.image.load("package/assets/images/inimigo_verde.png")
INIMIGO_AZUL = pygame.image.load("package/assets/images/inimigo_azul.png")

#img dos lasers
LASER_VERMELHO = pygame.image.load("package/assets/images/laser_vermelho.png")
LASER_VERDE = pygame.image.load("package/assets/images/laser_verde.png")
LASER_AZUL = pygame.image.load("package/assets/images/laser_azul.png")

class Inimigo(Nave):
        COLOR_MAP = {
                    "red": (INIMIGO_VERMELHO, LASER_VERMELHO),
                    "green": (INIMIGO_VERDE, LASER_VERDE),
                    "blue": (INIMIGO_AZUL, LASER_AZUL),
                    }

        def __init__(self, x, y, color, health=100):
            super().__init__(x, y, health)
            self.ship_img, self.laser_img = self.COLOR_MAP[color]
            self.mask = pygame.mask.from_surface(self.ship_img)

        def move(self, vel):
            self.y += vel

        def shoot(self):
            if self.cool_down_counter == 0:
                laser = Laser(self.x-20, self.y, self.laser_img)
                self.lasers.append(laser)
                self.cool_down_counter = 1
                
        def move_lasers(self, vel, obj, screen_height):
             return super().move_lasers(vel, obj, screen_height)
                