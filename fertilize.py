from time import sleep
from player import Player
import keyboard


sleep(2)
print("Start Fertilize Bot!")
player = Player()
player.REFILL_AMOUNT_PER_MAP = 20

try:
    while True:
        player.havestAll()
        player.plantAll()
        player.fertilizeAll()
        player.havestAll()
        player.refillEnergy()

except Exception as e:
    player.log(e)
    pass