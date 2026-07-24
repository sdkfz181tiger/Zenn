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

    def flip_x(self):
        """ x方向反転 """
        self.vx *= -1

    def intersects(self, other):
        """ 矩形同士の当たり判定(AABB) """
        if other.x + other.w < self.x: return False
        if self.x + self.w < other.x: return False
        if other.y + other.h < self.y: return False
        if self.y + self.h < other.y: return False
        return True

class ShipSprite(BaseSprite):

    def __init__(self, x, y):
        """ コンストラクタ """
        super().__init__(x, y)

    def draw(self):
        """ 描画処理 """
        pyxel.blt(self.x, self.y, 0, 
            0, 0, 
            self.w, self.h, 0) # Ship

class AsteroidSprite(BaseSprite):

    def __init__(self, x, y):
        """ コンストラクタ """
        super().__init__(x, y)
        self.index = random.randint(2, 7) # 隕石画像

    def draw(self):
        """ 描画処理 """
        pyxel.blt(self.x, self.y, 0, self.w*self.index, 0, 
                self.w, self.h, 0) # Ship

class BulletSprite(BaseSprite):

    def __init__(self, x, y):
        """ コンストラクタ """
        super().__init__(x, y)
        self.x += self.w / 2 - 1 # 中央に調整

    def draw(self):
        """ 描画処理 """
        pyxel.rect(self.x, self.y, 2, 2, 12)

class Star():

    def __init__(self, x, y, w, h):
        """ コンストラクタ """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = random.randint(0, 15)
        self.spd = random.randint(1, 3)

    def update(self):
        """ 更新処理 """
        self.y += self.spd
        if self.h < self.y: self.y = 0

    def draw(self):
        """ 描画処理 """
        pyxel.pset(self.x, self.y, self.c)

class Background():

    def __init__(self, w, h):
        """ コンストラクタ """
        self.w = w # ゲーム画面の幅
        self.h = h # ゲーム場面の高さ
        self.stars = [] # 星を管理するリスト
        for i in range(30):
            x = random.randint(0, w)
            y = random.randint(0, h)
            star = Star(x, y, self.w, self.h)
            self.stars.append(star)

    def update(self):
        """ 更新処理 """
        for star in self.stars:
            star.update()

    def draw(self):
        """ 描画処理 """
        for star in self.stars:
            star.draw()