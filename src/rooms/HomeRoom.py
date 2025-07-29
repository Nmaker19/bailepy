from Room import *
import pygame


class HomeRoom(Room):
    selected = 0
    font = None
    options = []

    def action_exit(self):
        self.app.is_running = False

    def on_create_room(self):
        self.options = [
            {
                'label': 'Nuevo Juego',
                'action': lambda: 0
            },
            {
                'label': 'Partidas',
                'action': lambda: 0
            },
            {
                'label': 'Configuracion',
                'action': lambda: 0
            },
            {
                'label': 'Salir',
                'action': self.action_exit
            }
        ]

        self.font = pygame.font.Font(self.app.RES / 'fonts' / 'Minecraft.ttf', 32)    
    
    def update(self, dt):
        if (pygame.K_UP in self.app.key_down):
            self.selected = max(0, self.selected - 1)

        if (pygame.K_DOWN in self.app.key_down):
            self.selected = min(len(self.options) - 1, self.selected + 1)
        
        if (pygame.K_RETURN in self.app.key_down):
            self.options[self.selected]['action']()
        

    def render(self, surface):
        i = 0
        for op in self.options:
            col = self.selected == i and (125, 125, 125) or (255, 255, 255)
            surface.blit(self.font.render(op['label'], False, col), (105, 105 + (i * 50)))
            i += 1
