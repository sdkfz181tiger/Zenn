# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random

class BaseSprite:

    def __init__(self, x, y, w=8, h=8):
        """ コンストラクタ """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vx = 0
        self.vy = 0

    def update(self):
        """ 更新処理 """
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        """ 描画処理(派生クラスで実装) """
        pass

    def move(self, spd, deg):
        """ 移動 """
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad) # x方向の速度
        self.vy = spd * math.sin(rad) # y方向の速度

    def intersects(self, other):
        """ 矩形同士の当たり判定(AABB) """
        if other.x + other.w < self.x: return False
        if self.x + self.w < other.x: return False
        if other.y + other.h < self.y: return False
        if self.y + self.h < other.y: return False
        return True

class PlayerSprite(BaseSprite):

    def __init__(self, x, y):
        """ コンストラクタ """
        super().__init__(x, y)
        self.gravity = 0.4 # 重力
        self.jump_x = 1.0 # ジャンプx
        self.jump_y = -3.4 # ジャンプy

    def update(self):
        """ 更新処理 """
        super().update()
        self.vy += self.gravity # Gravity

    def draw(self):
        """ 描画処理 """
        pyxel.blt(self.x, self.y, 0, 
            0, 16, self.w, self.h, 0)
        # Debug
        #pyxel.rectb(self.x, self.y, self.w, self.h, 3)

    def jump(self):
        """ ジャンプ """
        self.vx = self.jump_x # ジャンプx
        self.vy = self.jump_y # ジャンプy

class TunnelSprite(BaseSprite):

    def __init__(self, x, y, length, top_flg=False):
        """ コンストラクタ """
        super().__init__(x, y, 16, length*8)
        self.length = length # トンネルの長さ
        if(top_flg): self.y -= self.h # トンネル上

    def draw(self):
        """ 描画処理 """
        # Top
        pyxel.blt(self.x, self.y, 0, 
            16, 16, self.w, 8, 0)
        # Mid
        for i in range(self.length-2):
            y = self.y + (i+1)*8
            pyxel.blt(self.x, y, 0, 
                16, 24, self.w, 8, 0)
        # Bottom
        y = self.y + (self.length-1)*8
        pyxel.blt(self.x, y, 0, 
            16, 32, self.w, 8, 0)
        # Debug
        #pyxel.rectb(self.x, self.y, self.w, self.h, 3)