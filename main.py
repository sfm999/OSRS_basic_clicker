import pyautogui as gui
import resources.classes as pos
import numpy as np
import time


class Controller:
    def __init__(self):
        self.b = pos.Bank()
        self.i = pos.Inventory()
        self.prevX = 0
        self.prevY = 0
        self.rng = np.random.default_rng(12345)

    def fill_inventory_potion_making_part_one(self):
        self.move_to_and_left_click(self.b.lanta_x, self.b.lanta_y)
        self.move_to_and_left_click(self.b.water_x, self.b.water_y)
        self.close_bank()
        self.combine_pot_inventory()
        self.move_to_with_custom_duration(self.b.open_x, self.b.open_y, 1.2)
        time.sleep(7.8)
        self.open_bank()
        time.sleep(0.8)
        self.move_to_and_left_click(self.i.deposit_x, self.i.deposit_y)

    def fill_inventory_potion_making_part_two(self):
        self.move_to_and_left_click(self.b.lanta_x, self.b.lanta_y)
        self.move_to_and_left_click(self.b.water_x, self.b.water_y)
        self.close_bank()
        self.combine_pot_inventory()
        self.move_to_with_custom_duration(self.b.open_x, self.b.open_y, 1.2)
        time.sleep(17)
        self.open_bank()
        time.sleep(0.8)
        self.move_to_and_left_click(self.i.deposit_x, self.i.deposit_y)

    def combine_pot_inventory(self):
        self.move_to_and_left_click(self.i.lanta_x, self.i.lanta_y)
        self.move_to_and_left_click(self.i.water_x, self.i.water_y)
        time.sleep(0.6)
        gui.press('space')

    def move_to_with_custom_duration(self, x, y, duration):
        gui.moveTo(x, y, duration)

    def move_to_and_left_click(self, x, y):
        if self.prevX - x < 50 or self.prevY - y < 50:
            duration = self.rng.random()
        else:
            duration = self.rng.random() + 1
        gui.moveTo(x, y, duration, gui.easeInQuad)
        gui.leftClick()
        self.prevX = x
        self.prevY = y

    def open_bank(self):
        self.move_to_and_left_click(self.b.open_x, self.b.open_y)

    def close_bank(self):
        self.move_to_and_left_click(self.b.close_x, self.b.close_y)


if __name__ == '__main__':
    c = Controller()

    iterations = 5  # amount you want to loop
    count = 0       # counter for hitting iterations

    # MAIN LOOP
    c.open_bank()   # Open bank for loop
    time.sleep(1)
    while count < iterations:
        print(f"Loop %d" % count)
        c.fill_inventory_potion_making_part_two()    # function to make pots
        count += 1                          # increment counter

    c.close_bank()  # Close bank after loop
