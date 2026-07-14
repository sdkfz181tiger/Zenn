# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random

class BaseSprite:

    def __init__(self, x, y, u, v, spd, w=8, h=8):
        """ コンストラクタ """
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.spd = spd
        self.w = w
        self.h = h
        self.vx = 0
        self.vy = 0
        self.right_flg = True # 右向きフラグ

    def update(self):
        """ 更新処理 """
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        """ 描画処理 """
        u = 0 if self.right_flg else 8
        pyxel.blt(self.x, self.y, 0, 
            self.u + u, self.v, self.w, self.h, 0)

    def get_center(self):
        """ 中心座標 """
        return (self.x + self.w/2, self.y + self.h/2)

    def set_center(self, x, y):
        """ 中心座標 """
        self.x = x - self.w / 2
        self.y = y - self.h / 2

    def move(self, deg):
        """ 移動 """
        rad = (deg * math.pi) / 180
        self.vx = self.spd * math.cos(rad) # x方向の速度
        self.vy = self.spd * math.sin(rad) # y方向の速度
        if deg == 90 or deg == 270: return
        self.right_flg = not (90 < deg and deg < 270) # 右向きフラグ

    def stop(self):
        """ 停止 """
        self.vx = 0
        self.vy = 0

    def intersects(self, other):
        """ 矩形同士の当たり判定(AABB) """
        if other.x + other.w < self.x: return False
        if self.x + self.w < other.x: return False
        if other.y + other.h < self.y: return False
        if self.y + self.h < other.y: return False
        return True

    def contains_center(self, other):
        """ 矩形の中に中心座標が含まれるか """
        x, y = self.get_center()
        if other.x + other.w < x: return False
        if x < other.x: return False
        if other.y + other.h < y: return False
        if y < other.y: return False
        return True

    def get_distance(self, other):
        """ 距離を計算する """
        d_x = self.x - other.x
        d_y = self.y - other.y
        return math.sqrt(d_x*d_x + d_y*d_y)

    def get_direction(self, other):
        """ 方向を計算する """
        d_x = other.x - self.x
        d_y = other.y - self.y
        rad = math.atan2(d_y, d_x)
        return (rad * (180 / math.pi) + 360) % 360

class PlayerSprite(BaseSprite):

    def __init__(self, x, y, u, v, spd, game):
        """ コンストラクタ """
        super().__init__(x, y, u, v, spd)
        self.shot_interval = 24
        self.shot_counter = 0
        self.game = game

    def update(self):
        """ 更新処理 """
        super().update()
        # Shot
        self.shot_counter += 1
        if self.shot_interval < self.shot_counter:
            self.shot_counter = 0
            self.game.on_shot_event(self) # Shot

class Monster(BaseSprite):

    def __init__(self, x, y, obj, target):
        """ コンストラクタ """
        super().__init__(x, y, obj["u"], obj["v"], obj["spd"])
        self.wait_time = obj["wait_time"]
        self.move_time = obj["move_time"]
        self.target = target

        self.wait_flg = True
        self.action_time = 0

    def update(self):
        """ 更新処理 """
        super().update()
        # Time
        self.action_time += 1

        # 待機 or 移動
        if self.wait_flg:
            if self.wait_time < self.action_time:
                self.action_time = 0
                direction = self.get_direction(self.target)
                self.move(direction) # Move!!
                self.wait_flg = False
        else:
            if self.move_time < self.action_time:
                self.action_time = 0
                self.stop() # Wait!!
                self.wait_flg = True

class Bullet(BaseSprite):

    def __init__(self, x, y, spd, life=10):
        """ コンストラクタ """
        super().__init__(x, y, 0, 0, spd)
        self.life = life

    def update(self):
        """ 更新処理 """
        super().update()
        self.life -= 1
        if self.life < 0: 
            self.stop()

    def draw(self):
        """ 描画処理 """
        pyxel.rect(self.x, self.y, 1, 1, 7)

    def is_dead(self):
        """ 死亡フラグ """
        return self.life < 0

class Particle(BaseSprite):

    def __init__(self, x, y, life=10):
        """ コンストラクタ """
        super().__init__(x, y, 0, 0, 0)
        self.life = life

        self.area_r = 8
        self.circ_r = 0
        self.off_x = 0
        self.off_y = 0

    def update(self):
        """ 更新処理 """
        super().update()
        self.life -= 1
        if self.life < 0: 
            self.stop()

        self.circ_r = random.randint(2, 4)
        self.off_x = random.randint(0, self.area_r) - self.area_r / 2
        self.off_y = random.randint(0, self.area_r) - self.area_r / 2

    def draw(self):
        """ 描画処理 """
        colors = [2, 4, 8]
        pyxel.circ(
            self.x + self.off_x, 
            self.y + self.off_y, 
            self.circ_r, random.choice(colors))

    def is_dead(self):
        """ 死亡フラグ """
        return self.life < 0
