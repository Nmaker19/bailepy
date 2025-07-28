
class Room:
    room_id = None
    app = None

    def __init__(self, app):
        self.app = app

    # Actualizar
    def update(self, dt):
        pass

    # Dibujar
    def render(self, surface):
        pass

    # Cuando se crea la habitacion
    def on_create_room(self):
        pass

    # Cuando el juego entra en la habitacion
    def on_enter_room(self):
        pass

    # Cuando el juego sale de la habitacion
    def on_leave_room(self):
        pass

    # Cuando se destruye la habitacion
    def on_destroy_room(self):
        pass

