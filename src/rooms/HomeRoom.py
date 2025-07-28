from Room import *
import pygame

options = [
    {
        'label': 'Jugar',
    },
    {
        'label': 'Salir',
    }
]

class HomeRoom(Room):
    selected = 0
    font = None

    def on_create_room(self):
        self.font = pygame.font.Font(self.app.RES / 'fonts' / 'Minecraft.ttf', 32)    

    def render(self, surface):
        global options
        
        i = 0
        for op in options:
            col = self.selected == i and (255, 0, 0) or (255, 255, 255)
            surface.blit(self.font.render(op['label'], False, col), (105, 105 + (i * 50)))
            i += 1
