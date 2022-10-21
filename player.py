import os, pyautogui
from time import sleep
from datetime import datetime
from dotenv import load_dotenv
from random import uniform

load_dotenv("config.txt")

class Player:
    def __init__(self):

        self.PLANT_TYPE = os.getenv('PLANT_TYPE', "carrot")
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
        self.ROTTEN2_CONFIDENCE = float(os.getenv('ROTTEN2_CONFIDENCE', 0.8))
        self.FERTILIZE_CONFIDENCE = float(os.getenv('FERTILIZE_CONFIDENCE', 0.9))
        self.WARP_CONFIDENCE = float(os.getenv('WARP_CONFIDENCE', 0.7))
        self.AVATAR_CONFIDENCE = float(os.getenv('AVATAR_CONFIDENCE', 0.9))
        self.AVATAR2_CONFIDENCE = float(os.getenv('AVATAR2_CONFIDENCE', 0.9))
        self.REFILL_AMOUNT_PER_MAP = float(os.getenv('REFILL_AMOUNT_PER_MAP', 10))
        self.WAIT_DURATION_AFTER_WARP = float(os.getenv('WAIT_DURATION_AFTER_WARP', 10))
        self.RANDOM_CLICK_SIZE = float(os.getenv('RANDOM_CLICK_SIZE', 5))

        self.updatePos()

    def updatePos(self):
        self.empty = self.getAllPos("empty", self.EMPTY_CONFIDENCE)
        self.grow1 = self.getAllPos(self.PLANT_TYPE + "/grow1", self.GROW1_CONFIDENCE)
        self.grow2 = self.getAllPos(self.PLANT_TYPE + "/grow2", self.GROW2_CONFIDENCE)
        self.full = self.getAllPos(self.PLANT_TYPE + "/full", self.FULL_CONFIDENCE)
        self.rotten = self.getAllPos(self.PLANT_TYPE + "/rotten", self.ROTTEN_CONFIDENCE)
        self.rotten2 = self.getAllPos(self.PLANT_TYPE + "/rotten2", self.ROTTEN2_CONFIDENCE)
        self.warp = list(self.getAllPos("warp", self.WARP_CONFIDENCE))
        self.scissor = self.getPos("scissor")
        self.seed = self.getPos(self.PLANT_TYPE + "/seed") 
        self.fruit = self.getPos(self.PLANT_TYPE + "/fruit")
        self.fertilize = self.getPos("fertilize")
        #self.name = self.getPos("name")
        self.chat = self.getPos("chat")
        self.avatar = self.getPos("avatar", self.AVATAR_CONFIDENCE)
        self.avatar2 = self.getPos("avatar2", self.AVATAR2_CONFIDENCE)
        #if self.name :
        #    self.avatar = self.name + (0, 70)
    
    def havestAll(self):
        self.log("Harvest")
        self.walk(self.START_MAP_WALK_DIR, self.START_MAP_WALK_STEP)
        self.walk("right", 0.03)
        self.wait(0.5)
        self.updatePos()
        self.clickScissor()
        scissor_pos = self.scissor
        for f in list(self.full) + list(self.rotten) + list(self.rotten2):
            self.click(f)
            self.wait()
        self.wait(1)
        self.click(scissor_pos)
        self.move(self.chat)
    def plantAll(self):
        self.log("Plant")
        self.updatePos()
        self.clickSeed()
        seed_pos = self.seed
        for e in self.empty:
            self.click(e)
            self.wait()
        self.wait(1)
        self.click(seed_pos)
        self.move(self.chat)
    def fertilizeAll(self):
        self.log("Fertilize")
        self.updatePos()
        self.clickFertilize()
        fert_pos = self.fertilize
        for fe in list(self.grow1) + list(self.grow2):
            self.click(fe)
            self.wait()
        self.wait(1)
        self.click(fert_pos)
        self.move(self.chat)
    def refillEnergy(self):
        self.log("Refill")
        count = 0
        self.clickFruit()
        fruit_pos = self.fruit
        #self.walk("left")
        self.updatePos()
        while (self.avatar != None or self.avatar2 != None) and count < self.REFILL_AMOUNT_PER_MAP:
            if self.avatar != None:
                self.click([self.avatar[0], self.avatar[1]])
            else:
                self.click([self.avatar2[0], self.avatar2[1]])
            count = count+1
        #self.walk("right")
        self.wait(1)
        self.click(fruit_pos)
        self.move(self.chat)
    def warpNext(self):
        self.log("Warp")
        near = False
        count = 0
        while near == False and count < self.WARP_NEAR_TRY_LIMIT:
            self.updatePos()
            count = count+1
            self.wait()
            if self.warp != None and (self.avatar != None or self.avatar2 != None) and len(self.warp) != 0:
                self.warp.sort(key=lambda w: w[0], reverse = True)
                warp_left = self.warp[0][0]
                warp_down = self.warp[0][1]
                if self.avatar != None:
                    avatar_left = self.avatar[0]
                    avatar_down = self.avatar[1]
                else:
                    avatar_left = self.avatar2[0]
                    avatar_down = self.avatar2[1]
                if warp_left - avatar_left > self.WARP_NEAR_DECISION:
                    self.walk("right", self.WARP_NEAR_STEP)
                elif warp_left - avatar_left < self.WARP_NEAR_DECISION*-1:
                    self.walk("left", self.WARP_NEAR_STEP)
                elif warp_down - avatar_down > self.WARP_NEAR_DECISION:
                    self.walk("down", self.WARP_NEAR_STEP)
                elif warp_down - avatar_down < self.WARP_NEAR_DECISION*-1:
                    self.walk("up", self.WARP_NEAR_STEP)
                else:
                    near = True
                    self.click([warp_left+10, warp_down+10])
                    self.wait(self.WAIT_DURATION_AFTER_WARP)


    def clickScissor(self):
        if self.scissor != None:
            self.click(self.scissor)
    def clickFertilize(self):
        if self.fertilize != None:
            self.click(self.fertilize)
    def clickSeed(self):
        if self.seed != None:
            self.click(self.seed)
    def clickFruit(self):
        if self.fruit != None:
            self.click(self.fruit)

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
