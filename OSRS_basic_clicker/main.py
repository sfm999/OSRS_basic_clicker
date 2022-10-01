import numpy.random
import pyautogui as gui
import resources.classes as pos
import numpy as np
import time


class Controller:

    def __init__(self):
        self.b = pos.Bank()
        self.i = pos.Inventory()
        self.key = gui.press

    @staticmethod
    def left_click(x, y):
        # add variability
        x = int(x + np.random.random(1) * 15)
        y = int(y + np.random.random(1) * 15)
        duration = int(4 + np.random.random(1) * 5) / 10
        # move mouse & click
        gui.moveTo(x, y, duration, gui.easeInQuad)
        gui.leftClick()

    def open_bank(self):
        self.left_click(self.b.openX, self.b.openY)

    def target1(self):
        self.left_click(self.b.tar1X, self.b.tar1Y)

    def target2(self):
        self.left_click(self.b.tar2X, self.b.tar2Y)

    def depo(self):
        self.left_click(self.b.tar1X, self.b.tar1Y)

    def first(self):
        self.left_click(self.i.firstX, self.i.firstY)

    def third(self):
        self.left_click(self.i.thirdX, self.i.thirdY)

    def open_bank_jewel(self):
        self.left_click(self.b.bankJewelX, self.b.bankJewelY)

    def furnace(self):
        self.left_click(self.b.furnaceX, self.b.furnaceY)

    def jewel(self):
        self.left_click(self.b.jewelX, self.b.jewelY)

    def click_last(self):
        self.left_click(self.i.lastX, self.i.lastY)

    def cast_spell(self):
        self.left_click(self.i.spellX, self.i.spellY)

    def combine_at_bank(self):
        self.open_bank()
        # self.target1()
        self.first()
        self.target1()
        self.key('escape')
        self.left_click(self.i.fourteenthX, self.i.fourteenthY)
        self.left_click(self.i.fithteenthX, self.i.fithteenthY)
        # sl_time = 0.5 + np.random.rand(1)
        time.sleep(int(6 + np.random.random(1) * 5) / 10)
        self.key('space')
        time.sleep(int(1500 + np.random.random(1) * 300) / 100)

    def craft_jewel(self):
        self.open_bank_jewel()
        self.target1()
        self.third()
        self.target2()
        self.key('escape')
        self.furnace()
        time.sleep(10)
        self.jewel()
        time.sleep(30)

    def high_alch(self):
        cast_count = 0
        casts_to_count = 26

        self.open_bank()
        self.target1()
        self.key('escape')
        while cast_count < casts_to_count:
            self.cast_spell()
            time.sleep(int(30 + np.random.random(1) * 30) / 100)
            self.click_last()
            time.sleep(int(30 + np.random.random(1) * 30) / 100)
            cast_count += 1




if __name__ == '__main__':
    c = Controller()
    i = 60  # amount you want to loop
    k = 1  # counter for hitting iterations

    time.sleep(1)
    while k <= i:
        print(f"loop %d" % k)
        # c.combine_at_bank()
        c.high_alch()
        50
        k += 1
