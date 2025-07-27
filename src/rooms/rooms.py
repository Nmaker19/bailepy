from rooms.AfterGameRoom import *
from rooms.GameRoom import *
from rooms.HomeRoom import *
from rooms.IntroRoom import *

ROOMS = {
    'menu': AfterGameRoom,
    'game': GameRoom,
    'lose': HomeRoom,
    'intro': IntroRoom
}
