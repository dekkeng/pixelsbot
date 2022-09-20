from time import sleep
from player import Player
import keyboard


sleep(2)
print("Start Farm Bot!")
player = Player()

try:
    while True:
        player.havestAll()
        player.plantAll()
        player.refillEnergy()
        player.warpNext()

        sleep(10)
except Exception as e:
    player.log(e)
    pass