import pygame
import sys
from rooms.rooms import ROOMS

INITIAL_ROOM = 'intro'
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
TITLE = 'BailePy'


class App:
    fps = 60
    is_running = True
    rooms = {}
    current_room_id = 0
    id_incremental = 0
    exit_error = None
    screen_width = SCREEN_WIDTH
    screen_height = SCREEN_HEIGHT

    def load_room(self, name):
        self.id_incremental += 1
        key = self.id_incremental
        self.rooms[key] = ROOMS[name]()
        self.rooms[key].room_id = key
        self.rooms[key].on_create_room()
        return key
    
    def delete_room(self, name):
        if not name in self.rooms.keys(): return
        
        self.rooms[name].on_leave_room()
        self.rooms[name].on_destroy_room()
        del self.rooms[name]

        if name == self.current_room_id:
            self.exit_error = 'Habitacion actual eliminada'
            self.is_running = False
    
    def change_room(self, new):
        room_id = self.load_room(new)
        old_id = self.current_room_id
        self.set_room(room_id)
        self.delete_room(old_id)

        return room_id
    
    def change_room_cached(self, new):
        return self.set_room(self.load_room(new))

    def set_room(self, room_id):
        if self.current_room_id:
            self.rooms[self.current_room_id].on_leave_room()

        if not room_id in self.rooms.keys():
            self.exit_error = f'La habitacion {room_id} no existe en rooms'
            self.is_running = False

        self.current_room_id = room_id
        self.rooms[room_id].on_enter_room()

        return room_id

    def init(self):
        pygame.init()
        pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(TITLE)

        self.change_room(INITIAL_ROOM)
    
    def update(self):
        self.rooms[self.current_room_id].update()

    def render(self):
        self.rooms[self.current_room_id].render()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            
    def quit(self):
        if self.current_room_id:
            self.delete_room(self.current_room_id)

        pygame.quit()
        sys.exit()

    def run(self):
        self.init()
        
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        
        if self.exit_error:
            print('ERROR:', self.exit_error)

        self.quit()

