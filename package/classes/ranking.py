import json
import pygame

class Ranking:
    def __init__(self, max_entries=10):
        self.max_entries = max_entries
        self.entries = []
        self.load()
    
    def load(self):
        try:
            with open('ranking.json', 'r') as f:
                self.entries = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.entries = []
    
    def save(self):
        with open('ranking.json', 'w') as f:
            json.dump(self.entries, f, indent=2)
    
    def add_entry(self, name, score):
        entry = {
            'name': name.upper()[:3],  
            'score': score
        }
        self.entries.append(entry)
        self.entries.sort(key=lambda x: x['score'], reverse=True)
        self.entries = self.entries[:self.max_entries]
        self.save()

    def draw(self, screen, font, x, y):
        bg_width = 600 
        bg_height = 450 
        bg_x = screen.get_width() // 2 - bg_width // 2 
        bg_y = screen.get_height() // 2 - bg_height // 2 
    
        s = pygame.Surface((bg_width, bg_height), pygame.SRCALPHA)
        s.fill((30, 30, 60, 200))
        screen.blit(s, (bg_x, bg_y))

        pygame.draw.rect(screen, (0, 0, 100), (bg_x, bg_y, bg_width, bg_height), 3, border_radius=10)

        title_font = pygame.font.Font("package/assets/fonts/Pixellari.ttf", 45)
        title = title_font.render("TOP 10", True, (100, 255, 255))
        screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, bg_y + 20))
    
        pygame.draw.line(screen, (100, 255, 255), 
                   (bg_x + 50, bg_y + 70), 
                   (bg_x + bg_width - 50, bg_y + 70), 2)
    
        entry_start_y = bg_y + 90
        for i, entry in enumerate(self.entries[:10]):
            if i < 3:
                color = (255, 215, 0)
                entry_font = pygame.font.Font("package/assets/fonts/Pixellari.ttf", 32)
            else:
                color = (200, 200, 200)
                entry_font = font
            
            text = f"{i+1}. {entry['name']} - {entry['score']} PONTOS"
            entry_render = entry_font.render(text, True, color)
            text_x = screen.get_width() // 2 - entry_render.get_width() // 2
            screen.blit(entry_render, (text_x, entry_start_y + i * 35))
    