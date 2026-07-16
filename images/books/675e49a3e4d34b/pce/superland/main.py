# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random
import sprite

W, H = 160, 120

START_X = W / 4
START_Y = H / 2 - 16

MODE_TITLE     = "title"
MODE_PLAY      = "play"
MODE_GAME_OVER = "game_over"

CAMERA_PAD_X   = 60
CAMERA_LIMIT_L = W - 640
CAMERA_LIMIT_R = 0

# Game
class Game:
    def __init__(self):
        """ Constructor """

        # Pyxel
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")

        # Tilemap(Copy 0 -> 1)
        pyxel.tilemaps[1].blt(0, 0, 0, 0, 0, 640, 128)

        # Score
        self.score = 0

        # Game Mode
        self.game_mode = MODE_TITLE

        # Player
        self.player = sprite.PlayerSprite(START_X, START_Y, 16, 0)

        # Reset
        self.reset()

        # Run
        pyxel.run(self.update, self.draw)

    def update(self):

        # Score
        self.score = int(self.player.x - START_X)

        # Controll
        self.controll()

        # Game Mode
        if self.game_mode != MODE_PLAY: return

        # Player
        self.player.update()

        # x Obstacles, Items
        self.player.collide_obstacles()
        self.player.collide_items()

        # Game Over
        if H < self.player.y: 
            self.game_mode = MODE_GAME_OVER

    def draw(self):
        pyxel.cls(1)

        # Camera(on)
        self.camera_on()

        # Tilemap
        pyxel.bltm(0, 0, 0, 0, 0, 640, 128, 0)

        # Player
        self.player.draw()

        # Camera(off)
        self.camera_off()

        # Message
        if self.game_mode == MODE_TITLE:
            msg = "WASD TO PLAY"
            pyxel.text(W/2-len(msg)*2, 16, msg, 7)
        elif self.game_mode == MODE_GAME_OVER:
            msg = "GAME OVER"
            pyxel.text(W/2-len(msg)*2, 16, msg, 7)

        # Score
        pyxel.text(10, 10, 
            "SCORE:{:04}".format(self.score), 1)

    def reset(self):

        # Tilemap(1 -> 0)
        pyxel.tilemaps[0].blt(0, 0, 1, 0, 0, 640, 128) # Copy

        # Camera
        self.camera_x = 0

        # Reset
        self.player.reset(START_X, START_Y)

    def controll(self):

        # Game Mode
        if self.game_mode != MODE_PLAY:
            if not(pyxel.btnp(pyxel.KEY_W) or 
                pyxel.btnp(pyxel.KEY_A) or 
                pyxel.btnp(pyxel.KEY_S) or 
                pyxel.btnp(pyxel.KEY_D)):
                return

            # Title -> Play
            if self.game_mode == MODE_TITLE:
                self.game_mode = MODE_PLAY

            # Game Over -> Title
            if self.game_mode == MODE_GAME_OVER:
                self.game_mode = MODE_TITLE
                self.reset() # Reset
        else:
            # Player
            if pyxel.btnp(pyxel.KEY_W):
                self.player.jump()
            if pyxel.btnp(pyxel.KEY_A):
                self.player.runL()
            if pyxel.btnp(pyxel.KEY_D):
                self.player.runR()
            if pyxel.btnr(pyxel.KEY_A):
                self.player.stopLR()
            if pyxel.btnr(pyxel.KEY_D):
                self.player.stopLR()

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

def main():
    """ Main """
    Game()

if __name__ == "__main__":
    main()