from Room import *

class IntroRoom(Room):
    def on_enter_room(self):
        print('Room entered')
    
    def on_leave_room(self):
        print('Room leaved')
    
    def on_destroy_room(self):
        print('Room destroyed')
