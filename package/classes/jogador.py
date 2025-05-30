import pygame
from pygame.locals import *
from package.classes.nave import Nave

#img do jogador
NAVE_Jogador = pygame.image.load("package/assets/images/nave_jogador.png")
#img do laser
LASER_Jogador = pygame.image.load("package/assets/images/laser_jogador.png")


class Jogador(Nave):
    def __init__(self, x, y, health=150):
        super().__init__(x, y, health)
        self.ship_img = NAVE_Jogador
        self.laser_img = LASER_Jogador
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs, screen_height): 
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(screen_height):
                self.lasers.remove(laser)
            else:
                for obj in objs[:]:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)
                        return 15
        return 0
    
    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))