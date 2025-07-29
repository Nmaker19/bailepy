from Room import *
from pathlib import Path
from threading import Timer
import pygame

class IntroRoom(Room):
    font = None
    intro_timer = None
    x = 0

    def on_timeout(self):   
        print('timeout')
        self.app.change_room('menu')
        pass

    def on_create_room(self):
        self.font = pygame.font.Font(self.app.RES / 'fonts' / 'Minecraft.ttf', 32)
        self.intro_timer = Timer(5, self.on_timeout)
        self.intro_timer.start()
        

    def update(self, dt):
        self.x += 35 * dt

    def render(self, surface):
    	surface.blit(self.font.render('Desarrollado por Nmaker19 y Technolobito', False, (125, 0, 0)), (self.x, self.x))
