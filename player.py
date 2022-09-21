import os, pyautogui
from time import sleep
from datetime import datetime
from dotenv import load_dotenv
from random import uniform

load_dotenv("config.txt")

class Player:
    def __init__(self):

        self.START_MAP_WALK_DIR = os.getenv('START_MAP_WALK_DIR', "down")
        self.START_MAP_WALK_STEP = float(os.getenv('START_MAP_WALK_STEP', 0.1))
        self.WARP_NEAR_DECISION = float(os.getenv('WARP_NEAR_DECISION', 150))
        self.WARP_NEAR_STEP = float(os.getenv('WARP_NEAR_STEP', 0.3))
        self.WARP_NEAR_TRY_LIMIT = float(os.getenv('WARP_NEAR_TRY_LIMIT', 100))
        self.EMPTY_CONFIDENCE = float(os.getenv('EMPTY_CONFIDENCE', 0.6))
        self.GROW1_CONFIDENCE = float(os.getenv('GROW1_CONFIDENCE', 0.8))
        self.GROW2_CONFIDENCE = float(os.getenv('GROW2_CONFIDENCE', 0.8))
        self.FULL_CONFIDENCE = float(os.getenv('FULL_CONFIDENCE', 0.75))
        self.ROTTEN_CONFIDENCE = float(os.getenv('ROTTEN_CONFIDENCE', 0.75))
        self.FERTILIZE_CONFIDENCE = float(os.getenv('FERTILIZE_CONFIDENCE', 0.9))
        self.WARP_CONFIDENCE = float(os.getenv('WARP_CONFIDENCE', 0.7))
        self.REFILL_AMOUNT_PER_MAP = float(os.getenv('REFILL_AMOUNT_PER_MAP', 10))
        self.WAIT_DURATION_AFTER_WARP = float(os.getenv('WAIT_DURATION_AFTER_WARP', 10))
        self.RANDOM_CLICK_SIZE = float(os.getenv('RANDOM_CLICK_SIZE', 5))

        self.updatePos()

    def updatePos(self):
        self.empty = self.getAllPos("empty", self.EMPTY_CONFIDENCE)
        self.grow1 = self.getAllPos("grow1", self.GROW1_CONFIDENCE)
        self.grow2 = self.getAllPos("grow2", self.GROW2_CONFIDENCE)
        self.full = self.getAllPos("full", self.FULL_CONFIDENCE)
        self.rotten = self.getAllPos("rotten", self.ROTTEN_CONFIDENCE)
        self.warp = list(self.getAllPos("warp", self.WARP_CONFIDENCE))
        self.scissor = self.getPos("scissor")
        self.seed = self.getPos("seed") 
        self.carrot = self.getPos("carrot")
        self.fertilize = self.getPos("fertilize")
        self.name = self.getPos("name")
        self.chat = self.getPos("chat")
        self.body = None
        if self.name :
            self.body = self.name + (0, 70)
    
    def havestAll(self):
        self.log("Harvest")
        self.walk(self.START_MAP_WALK_DIR, self.START_MAP_WALK_STEP)
        self.updatePos()
        self.clickScissor()
        for f in list(self.full) + list(self.rotten):
            self.click(f)
            self.wait()
        self.clickScissor()
        self.move(self.chat)
        self.wait(1)
    def plantAll(self):
        self.log("Plant")
        self.updatePos()
        self.clickSeed()
        for e in self.empty:
            self.click(e)
            self.wait()
        self.wait(1)
        self.move(self.chat)
    def fertilizeAll(self):
        self.log("Fertilize")
        self.updatePos()
        self.clickFertilize()
        for fe in list(self.grow1) + list(self.grow2):
            self.click(fe)
            self.wait()
        self.wait(1)
        self.move(self.chat)
    def refillEnergy(self):
        self.log("Refill")
        count = 0
        self.clickCarrot()
        #self.walk("left")
        self.updatePos()
        while self.body != None and count < self.REFILL_AMOUNT_PER_MAP:
            self.click(self.body)
            count = count+1
        #self.walk("right")
        self.move(self.chat)
    def warpNext(self):
        self.log("Warp")
        near = False
        count = 0
        while near == False and count < self.WARP_NEAR_TRY_LIMIT:
            self.updatePos()
            count = count+1
            self.wait()
            if self.warp != None and self.body != None and len(self.warp) != 0:
                self.warp.sort(key=lambda w: w[0], reverse = True)
                warp_left = self.warp[0][0]
                body_left = self.body[0]
                warp_down = self.warp[0][1]
                body_down = self.body[1]
                if warp_left - body_left > self.WARP_NEAR_DECISION:
                    self.walk("right", self.WARP_NEAR_STEP)
                elif warp_left - body_left < self.WARP_NEAR_DECISION*-1:
                    self.walk("left", self.WARP_NEAR_STEP)
                elif warp_down - body_down > self.WARP_NEAR_DECISION:
                    self.walk("down", self.WARP_NEAR_STEP)
                elif warp_down - body_down < self.WARP_NEAR_DECISION*-1:
                    self.walk("up", self.WARP_NEAR_STEP)
                else:
                    near = True
                    self.click([warp_left+10, warp_down+10])
                    self.wait(self.WAIT_DURATION_AFTER_WARP)


    def clickScissor(self):
        self.click(self.scissor)
    def clickFertilize(self):
        self.click(self.fertilize)
    def clickSeed(self):
        self.click(self.seed)
    def clickCarrot(self):
        self.click(self.carrot)

    def getPos(self, file, conf = 0.6):
        return pyautogui.locateCenterOnScreen('./sample/'+file+'.png', confidence = conf)

    def getAllPos(self, file, conf = 0.7):
        return pyautogui.locateAllOnScreen('./sample/'+file+'.png', confidence = conf)

    def walk(self, dir, length = 0.05):
        pyautogui.keyDown(dir)
        self.wait(length)
        pyautogui.keyUp(dir)
    def wait(self, length = 0.01):
        sleep(uniform(length-0.01, length+0.01))

    def move(self, pos):
        pyautogui.moveTo(pos)
        
    def click(self, pos):
        pyautogui.click([uniform(pos[0], pos[0]+self.RANDOM_CLICK_SIZE), uniform(pos[1], pos[1]+self.RANDOM_CLICK_SIZE)])
        
    def log(self, msg):
        """Msg log"""
        t = datetime.now().strftime('%H:%M:%S')
        print(f'[{t}] MESSAGE: {msg}')
