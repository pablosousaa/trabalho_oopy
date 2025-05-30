import pygame
import os
import time
import random
from pygame.locals import *
from package.classes.jogador import Jogador
from package.classes.inimigos import Inimigo
from package.classes.ranking import Ranking

screen = pygame.display.set_mode((1280, 720))

class LabSpace:
    
    
    def __init__(self, screen):        
        # Background
        self.ranking = Ranking()
        self.WIDTH, self.HEIGHT = 1280, 720
        self.BG = None
        self.WIN = screen 
        self.pontos = 0
 
    def collide(self, obj1, obj2):
        offset_x = obj2.x - obj1.x
        offset_y = obj2.y - obj1.y
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

    def game_over(self):
        self.entering_name = True
        self.input_name = "" 
        font = pygame.font.Font("package/assets/fonts/Pixellari.ttf", 36)
        big_font = pygame.font.Font("package/assets/fonts/Pixellari.ttf", 72)
    
        while self.entering_name:
            screen.fill("black")
        
            score_line1 = big_font.render("VOCÊ PERDEU!", True, (255, 0, 0))
            score_line2 = font.render(f"SUA PONTUAÇÃO FOI DE {self.pontos} PONTOS!", True, (255, 255, 255))
            self.WIN.blit(score_line1, (self.WIDTH//2 - score_line1.get_width()//2, 100))
            self.WIN.blit(score_line2, (self.WIDTH//2 - score_line2.get_width()//2, self.HEIGHT//2 - 30))
            input_line1 = font.render("DIGITE SUAS INICIAIS DE RANK ABAIXO:", True, (255, 255, 255))
            input_line2 = big_font.render(self.input_name, True, (0, 255, 0))
            self.WIN.blit(input_line1, (self.WIDTH//2 - input_line1.get_width()//2, self.HEIGHT//2 + 20))
            self.WIN.blit(input_line2, (self.WIDTH//2 - input_line2.get_width()//2, self.HEIGHT//2 + 90))
        
            pygame.display.update()
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(self.input_name) == 3:
                        self.ranking.add_entry(self.input_name, self.pontos)
                        self.entering_name = False
                        return False
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_name = self.input_name[:-1]
                    elif len(self.input_name) < 3 and event.unicode.isalpha():
                        self.input_name += event.unicode.upper()
        return False
                    
    def main(self):
        run = True
        FPS = 60
        level = 0
        lives = 1
        self.pontos = 0
        
        main_font = pygame.font.Font("package/assets/fonts/Pixellari.ttf", 50)
        lost_font = pygame.font.Font("package/assets/fonts/Pixellari.ttf", 50)

        inimigo = []
        wave_length = 5
        inimigo_vel = 1

        jogador_vel = 7
        laser_vel = 5

        jogador = Jogador(600, 500)

        clock = pygame.time.Clock()

        lost = False
        lost_count = 0

        def redraw_window():
            screen.fill("black")
            # draw text
            lives_label = main_font.render(f"Vidas: {lives}", 1, (255,255,255))
            level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
            pontos_label = main_font.render(f"Pontos: {self.pontos}", 1, (255,255,255))

            self.WIN.blit(lives_label, (10, 10))
            self.WIN.blit(level_label, (self.WIDTH - level_label.get_width() - 10, 10))
            self.WIN.blit(pontos_label, (self.WIDTH//2 - pontos_label.get_width()//2, 10))

            for Inimigo in inimigo:
                Inimigo.draw(self.WIN)

            jogador.draw(self.WIN)

            pygame.display.flip()

        while run:
            clock.tick(FPS)
            redraw_window()

            if lives <= 0 or jogador.health <= 0:
                lost = True
                lost_count += 1
                if lost_count == 1:
                    if self.game_over():
                        return True
                    else:
                        return False

            if lost:
                if lost_count > FPS * 3:
                    run = False
                else:
                    continue
                self.ranking.draw(self.WIN, main_font, 50, 400)

            if len(inimigo) == 0:
                level += 1
                wave_length += 5
                for i in range(wave_length):
                    novo_inimigo = Inimigo(random.randrange(50, self.WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                    inimigo.append(novo_inimigo)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and jogador.x - jogador_vel > 0: #esquerda
                jogador.x -= jogador_vel
            if keys[pygame.K_RIGHT] and jogador.x + jogador_vel + jogador.get_width() < self.WIDTH: #direita
                jogador.x += jogador_vel
            if keys[pygame.K_UP] and jogador.y - jogador_vel > 0: #cima
                jogador.y -= jogador_vel
            if keys[pygame.K_DOWN] and jogador.y + jogador_vel + jogador.get_height() + 15 < self.HEIGHT: #baixo
                jogador.y += jogador_vel
            if keys[pygame.K_SPACE]:
                jogador.shoot()

            for inimigo_obj in inimigo[:]:
                inimigo_obj.move(inimigo_vel)
                inimigo_obj.move_lasers(laser_vel, jogador, self.HEIGHT)

                if random.randrange(0, 2*60) == 1:
                    inimigo_obj.shoot()

                if self.collide(inimigo_obj, jogador):
                    jogador.health -= 10
                    inimigo.remove(inimigo_obj)
                elif inimigo_obj.y + inimigo_obj.get_height() > self.HEIGHT:
                    lives -= 1
                    inimigo.remove(inimigo_obj)

            pontos_ganhos = jogador.move_lasers(-laser_vel, inimigo, self.HEIGHT)
            self.pontos += pontos_ganhos * (level + 1)
            
    def run(self):
        should_restart = self.main()
        return should_restart
    
