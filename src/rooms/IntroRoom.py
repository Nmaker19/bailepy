from Room import *
from pathlib import Path
import pygame

class IntroRoom(Room):
    font = None

    def on_create_room(self):
        self.font = pygame.font.Font((Path(__file__).parent / '..' / 'res' / 'fonts' / 'Minecraft.ttf').resolve() , 32)

    def update(self, dt):
        pass
    
    def render(self, surface):
        surface.blit(self.font.render('Hola mundo!', False, (125, 0, 0)), (105, 105))
        surface.blit(self.font.render('Hola mundo!', False, (255, 255, 255)), (100, 100))


