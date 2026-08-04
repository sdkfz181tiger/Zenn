# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random

W, H = 128, 128

VEL_X     = 0.8
VEL_Y     = 0.8
GRAVITY_X = -0.01
GRAVITY_Y = 0.02

class BaseSprite:

    def __init__(self, x, y, u, v, w=8, h=8):
        """ Constructor """
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.vx = 0
        self.vy = 0

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        pyxel.blt(self.x, self.y, 0,
            self.u, self.v,
            self.w, self.h, 0)

    @property
    def center(self):
        return self.x + self.w/2, self.y + self.h/2

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.w

    @property
    def top(self):
        return self.y

    @property
    def bottom(self):
        return self.y + self.h

    def contains(self, spr):
        x, y = spr.center
        if x < self.left: return False
        if y < self.top: return False
        if self.right < x: return False
        if self.bottom < y: return False
        return True

class PlayerSprite(BaseSprite):

    def __init__(self, x, y, u, v):
        """ Constructor """
        super().__init__(x, y, u, v, 16, 16)
        self.vx = 0
        self.vy = -VEL_Y
        self.accel_flg = False

    def update(self):
        super().update()
        # Accel
        if self.accel_flg:
            self.vx = VEL_X
            self.vy = VEL_Y
        else:
            # Gravity
            self.vx += GRAVITY_X
            self.vy += GRAVITY_Y

    def action_press(self):
        self.accel_flg = True
        self.u = 32

    def action_release(self):
        self.accel_flg = False
        self.u = 16
        self.vx = 0
        self.vy = -VEL_Y

class CloudSprite(BaseSprite):

    def __init__(self, x, y, u, v, w, h):
        """ Constructor """
        super().__init__(x, y, u, v, w, h)
        self.vx = 0
        self.vy = 0

    def slide(self, vx):
        self.vx = vx

class ItemSprite(BaseSprite):

    def __init__(self, x, y, u, v):
        """ Constructor """
        super().__init__(x, y, u, v)
        self.vx = 0
        self.vy = 0

    def slide(self, vx):
        self.vx = vx

# Game
class Game:
    def __init__(self):
        """ Constructor """

        # Pyxel
        pyxel.init(W, H, title="Hello, Pyxel!!", fps=32)
        pyxel.load("my_resource.pyxres")

        # Score
        self.score = 0

        # Player
        self.player = PlayerSprite(
            20, H/2, 16, 0)

        # Inverval
        self.interval_cnt = 0
        self.interval_limit = 32

        # Items
        self.items = []

        # Clouds
        self.cloud_w = 32
        self.cloud_h = 16
        self.cloud_vx = -0.4
        self.clouds_top = []
        for i in range(0, 6):
            x = i * self.cloud_w
            cloud = CloudSprite(
                x, -4, 0, 56, self.cloud_w, self.cloud_h)
            cloud.slide(self.cloud_vx)# slide
            self.clouds_top.append(cloud)

        self.clouds_bottom = []
        for i in range(0, 6):
            x = i * self.cloud_w
            cloud = CloudSprite(
                x, H - 12, 0, 72, self.cloud_w, self.cloud_h)
            cloud.slide(self.cloud_vx)# slide
            self.clouds_bottom.append(cloud)

        # Run
        pyxel.run(self.update, self.draw)

    def update(self):

        # Controll
        self.controll()

        # Player
        self.player.update()

        # LRTB
        if self.player.left < 0:
            self.player.x = 0
        if W < self.player.right:
            self.player.x = W - self.player.w
        if self.player.top < 0:
            self.player.y = 0
        if H < self.player.bottom:
            self.player.y = H - self.player.h

        # Interval
        self.interval_cnt += 1
        if self.interval_limit < self.interval_cnt:
            self.interval_cnt = random.randint(16, 32)
            self.create_item() # Item

        # Items
        for i in range(len(self.items)-1, 0, -1):
            item = self.items[i]
            item.update()
            if item.right < 0:
                self.items.pop(i)
                continue
            if self.player.contains(item):
                self.items.pop(i)
                self.score += 10 # Score
                pyxel.play(0, 0, loop=False) # Sound

        # Clouds
        for cloud in self.clouds_top:
            cloud.update()
            if cloud.right < 0:
                cloud.x = cloud.x + self.cloud_w * len(self.clouds_top)

        for cloud in self.clouds_bottom:
            cloud.update()
            if cloud.right < 0:
                cloud.x = cloud.x + self.cloud_w * len(self.clouds_bottom)

    def draw(self):

        # Clear
        pyxel.cls(0)

        # Tilemap
        pyxel.bltm(0, 0, 0, 0, 0, 128, 128, 0)

        # Player
        self.player.draw()

        # Items
        for item in self.items:
            item.draw()

        # Clouds
        for cloud in self.clouds_top:
            cloud.draw()
        for cloud in self.clouds_bottom:
            cloud.draw()

        # Score
        pyxel.text(1, 1, 
            "SCORE:{:03}".format(self.score), 7)

    def controll(self):
        # Btn
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            print("pressed!!")
            self.player.action_press()
        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            print("released!!")
            self.player.action_release()

    def create_item(self):
        print("create_item")
        # Coin
        y = random.randint(0, H - 16)
        vx = 0.2 + random.random()
        item = ItemSprite(W, y, 0, 16)
        item.slide(-vx) # Slide
        self.items.append(item)

def main():
    """ Main """
    Game()

if __name__ == "__main__":
    main()