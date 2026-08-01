# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random

W, H = 128, 128

START_R = 7
START_C = 8

CAMERA_PAD_X   = 0
CAMERA_LIMIT_L = -W
CAMERA_LIMIT_R = W

TILE_NONE  = 0
TILE_COIN  = 1
TILE_BLOCK = 2

# u, v
TILE_COINS = {
    (0, 2): TILE_COIN
}

# u, v
TILE_BLOCKS = {
    (0, 4): TILE_BLOCK, (1, 4): TILE_BLOCK,
    (2, 4): TILE_BLOCK, (3, 4): TILE_BLOCK,
    (4, 4): TILE_BLOCK, (5, 4): TILE_BLOCK, 
    (6, 4): TILE_BLOCK, (7, 4): TILE_BLOCK,
    (0, 5): TILE_BLOCK, (1, 5): TILE_BLOCK,
    (2, 5): TILE_BLOCK, (3, 5): TILE_BLOCK,
    (0, 6): TILE_BLOCK, (1, 6): TILE_BLOCK,
    (2, 6): TILE_BLOCK, (3, 6): TILE_BLOCK
}

class BaseSprite:

    def __init__(self, x, y, u, v, w=8, h=8):
        """ Constructor """
        self.x    = x
        self.y    = y
        self.u    = u
        self.v    = v
        self.w    = w
        self.h    = h
        self.to_x = x
        self.to_y = y
        self.vx   = 0
        self.vy   = 0

    def update(self):
        dx = self.to_x - self.x
        dy = self.to_y - self.y

        if abs(dx) < 4:
            self.x = self.to_x
            self.vx = 0
        else:
            self.x += self.vx

        if abs(dy) < 4:
            self.y = self.to_y
            self.vy = 0
        else:
            self.y += self.vy

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 
            self.u, self.v,
            self.w, self.h, 0)

    def go(self, spd, to_u, to_v):
        if self.is_moving(): return False
        self.to_x = to_u * 8
        self.to_y = to_v * 8
        dx = self.to_x - self.x
        dy = self.to_y - self.y
        if dx == 0 and dy == 0: return False
        rad = math.atan2(dy, dx)
        self.vx = math.cos(rad) * spd
        self.vy = math.sin(rad) * spd
        return True

    def is_moving(self):
        if self.x != self.to_x: return True
        if self.y != self.to_y: return True
        return False

class PlayerSprite(BaseSprite):

    def __init__(self, x, y, u, v):
        """ Constructor """
        super().__init__(x, y, u, v)

    def update(self):
        super().update()

    def draw(self):
        super().draw()
        if not self.is_moving(): return
        dx = self.to_x - self.x
        dy = self.to_y - self.y

        # Left or Right
        if dx == 0:
            pass
        elif 0 < dx:
            pyxel.blt(self.x-8, self.y, 0, 
                self.u+16, self.v,
                self.w, self.h, 0)
        else:
            pyxel.blt(self.x+8, self.y, 0, 
                self.u+24, self.v,
                self.w, self.h, 0)

        # Up or Down
        if dy == 0:
            pass
        elif 0 < dy:
            pyxel.blt(self.x, self.y-8, 0, 
                self.u+16, self.v+8,
                self.w, self.h, 0)
        else:
            pyxel.blt(self.x, self.y+8, 0, 
                self.u+24, self.v+8,
                self.w, self.h, 0)

# Game
class Game:
    def __init__(self):
        """ Constructor """

        # Pyxel
        pyxel.init(W, H, title="Hello, Pyxel!!", fps=50)
        pyxel.load("my_resource.pyxres")

        # Tilemap(Copy 0 -> 1)
        pyxel.tilemaps[1].blt(0, 0, 0, 0, 0, 640, 128)

        # Score
        self.score = 0
        # Counter
        self.coin_total = self.count_coins()
        self.coin_rest = self.coin_total

        # Camera
        self.camera_x = 0

        # Player
        self.player = PlayerSprite(
            START_C * 8, START_R * 8, 16, 0)

        # Run
        pyxel.run(self.update, self.draw)

    def update(self):

        # Controll
        self.controll()

        # Player
        self.player.update()

        # Player x Coins
        u, v = self.get_uv(self.player.x, self.player.y)
        tile = self.get_tile(u, v)
        if tile in TILE_COINS:
            self.score += 1 # Score
            self.coin_rest -= 1 # Counter
            self.set_tile(u, v, (0, 0)) # Delete
            if 0 < self.coin_rest:
                pyxel.play(1, 4, loop=False) # Sound
            else:
                pyxel.play(1, 6, loop=False) # Sound

    def draw(self):

        # Clear
        pyxel.cls(0)

        # Camera(on)
        self.camera_on()

        # Tilemap
        pyxel.bltm(0, 0, 0, 0, 0, 640, 128, 0)

        # Player
        self.player.draw()

        # Camera(off)
        self.camera_off()

        # ポイント2: スコア、残りコイン表示
        # Score
        #pyxel.text(1, 1, 
        #   "SCORE:{:03}".format(self.score), 7)

        # Rest
        #pyxel.text(80, 1, 
        #   "REST:{:03}/{:03}".format(self.coin_rest, self.coin_total), 7)

        # CLEAR
        if self.coin_rest <= 0:
            pyxel.text(42, H-8, "GAME CLEAR!!", 7)

    def controll(self):
        # Player
        from_u, from_v = self.get_uv(self.player.x, self.player.y)

        if pyxel.btnp(pyxel.KEY_W):
            to_u, to_v = self.search_block(from_u, from_v, 0, -1)
            if self.player.go(4, to_u, to_v):
                pyxel.play(0, 0, loop=False) # Sound
            else:
                pyxel.play(0, 8, loop=False) # Sound
            return

        # ポイント1: コントロール & サウンド
        # if pyxel.btnp(pyxel.xxx):
        #     to_u, to_v = self.search_block(from_u, from_v, 0, 0)
        #     if self.player.go(4, to_u, to_v):
        #         pyxel.play(0, 0, loop=False) # Sound
        #     else:
        #         pyxel.play(0, 8, loop=False) # Sound
        #     return

        # if pyxel.btnp(pyxel.xxx):
        #     to_u, to_v = self.search_block(from_u, from_v, 0, 0)
        #     if self.player.go(4, to_u, to_v):
        #         pyxel.play(0, 0, loop=False) # Sound
        #     else:
        #         pyxel.play(0, 8, loop=False) # Sound
        #     return

        # if pyxel.btnr(pyxel.xxx):
        #     to_u, to_v = self.search_block(from_u, from_v, 0, 0)
        #     if self.player.go(4, to_u, to_v):
        #         pyxel.play(0, 0, loop=False) # Sound
        #     else:
        #         pyxel.play(0, 8, loop=False) # Sound
        #     return

    def camera_on(self):
        line_r = W - self.camera_x - CAMERA_PAD_X
        if line_r < self.player.x:
            self.camera_x += line_r - self.player.x
            if self.camera_x < CAMERA_LIMIT_L:
                self.camera_x = CAMERA_LIMIT_L
        line_l = 0 - self.camera_x + CAMERA_PAD_X
        if self.player.x < line_l:
            self.camera_x += line_l - self.player.x
            if CAMERA_LIMIT_R < self.camera_x:
                self.camera_x = CAMERA_LIMIT_R
        pyxel.camera(-self.camera_x, 0)

    def camera_off(self):
        pyxel.camera()

    def get_uv(self, x, y):
        return (x//8, y//8)

    def get_tile(self, u, v):
        return pyxel.tilemaps[0].pget(u, v)

    def set_tile(self, u, v, tile):
        pyxel.tilemaps[0].pset(u, v, tile)

    def search_block(self, from_u, from_v, off_u, off_v):
        to_u = from_u + off_u
        to_v = from_v + off_v
        if to_u < 0: return from_u, from_v
        if to_v < 0: return from_u, from_v
        if 15 < to_u: return from_u, from_v
        if 15 < to_v: return from_u, from_v
        # ポイント3: 衝突判定
        # tile = self.get_tile(to_u, to_v)
        # if tile in TILE_BLOCKS:
        #     return from_u, from_v

        return self.search_block(to_u, to_v, off_u, off_v)

    def count_coins(self):
        tilemap = pyxel.tilemaps[0]
        w = tilemap.width
        h = tilemap.height
        counter = 0
        for u in range(w):
            for v in range(h):
                tile = tilemap.pget(u, v)
                if tile in TILE_COINS:
                    counter += 1
        return counter

def main():
    """ Main """
    Game()

if __name__ == "__main__":
    main()