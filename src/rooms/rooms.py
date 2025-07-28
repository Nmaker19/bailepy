from rooms.AfterGameRoom import *
from rooms.GameRoom import *
from rooms.HomeRoom import *
from rooms.IntroRoom import *

ROOMS = {
    'menu': HomeRoom,
    'game': GameRoom,
    'after': AfterGameRoom,
    'intro': IntroRoom
}
