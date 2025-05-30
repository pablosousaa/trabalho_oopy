import pygame, sys
from pygame.locals import *
from package.classes.button import Button
from package.classes.controlador import LabSpace
from package.classes.ranking import Ranking

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
BG = pygame.image.load("package/assets/images/background.png")

class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Menu")
        self.BG = pygame.image.load("package/assets/images/background.png")
        self.labspace = LabSpace(self.screen)
    
    def rank(self): #tela de ranking
        ranking = Ranking()
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            screen.fill("black")
        
            RANK_TEXT = self.get_font(60).render("RANKING GERAL", True, "White")
            RANK_RECT = RANK_TEXT.get_rect(center=(640, 100))
            screen.blit(RANK_TEXT, RANK_RECT)
        
            ranking.draw(screen, self.get_font(30), 340, 180)
        
            PLAY_BACK = Button(image=None, pos=(640, 650), 
                         text_input="VOLTAR", font=self.get_font(60), base_color="White", hovering_color="Green")
            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(screen)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.main_menu()
        
            pygame.display.update()
        
    def get_font(self, size): #funçao para definir a fonte e tamanho das palavras
        return pygame.font.Font("package/assets/fonts/Pixellari.ttf", size)

    def play(self): #tela do jogo 
        while True:
            
            should_continue = self.labspace.run()  #executa o jogo
            if not should_continue:
                break
        self.main_menu()
        

    def main_menu(self): #interfaçe do menu inicial 
        pygame.display.set_caption("LabSpace") 

        while True:
            screen.blit(BG, (0, 0))
        
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("LABSPACE", True, "White")
            MENU_RECT = MENU_TEXT.get_rect(center = (640, 150))

            PLAY_BUTTON = Button(image=pygame.image.load("package/assets/images/Play Rect.png"), pos=(640, 300), 
                            text_input="JOGAR", font=self.get_font(75), base_color="#bdffd6", hovering_color="White")
            RANK_BUTTON = Button(image=pygame.image.load("package/assets/images/Tecla Rect.png"), pos=(640, 450), 
                            text_input="RANK", font=self.get_font(75), base_color="#bdffd6", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("package/assets/images/Sair Rect.png"), pos=(640, 600), 
                            text_input="SAIR", font=self.get_font(75), base_color="#bdffd6", hovering_color="White")
            screen.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, RANK_BUTTON, QUIT_BUTTON,]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.play()
                    if RANK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.rank()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

'''
    def opcoes(self): #tela de controles
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            screen.fill("black")

            PLAY_TEXT = self.get_font(45).render("Configurações em desenvovilemto...", True, "White")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
            screen.blit(PLAY_TEXT, PLAY_RECT)

            PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="VOLTAR", font=self.get_font(75), base_color="White", hovering_color="Green")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.main_menu()

            pygame.display.update()
'''
