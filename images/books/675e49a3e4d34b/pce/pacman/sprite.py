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
        self.right_flg = False # 右向きフラグ
        self.u_anim_cnt = 0 # Animation
        self.u_anim_max = 6 # Animation

    def update(self):
        """ 更新処理 """
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        """ 描画処理 """
        # Animation
        self.u_anim_cnt += 1
        if self.u_anim_max < self.u_anim_cnt: self.u_anim_cnt = 0
        u = self.u_anim_cnt * 8
        v = 0 if self.right_flg else 8
        pyxel.blt(self.x, self.y, 0, 
            self.u + u, self.v + v, self.w, self.h, 0)

    def get_center(self):
        """ 中心座標 """
        return (self.x + self.w/2, self.y + self.h/2)

    def set_center(self, x, y):
        """ 中心座標 """
        self.x = x - self.w / 2
        self.y = y - self.h / 2

    def swap_position(self, other):
        """ 座標交換 """
        x = self.x
        y = self.y
        self.x = other.x
        self.y = other.y
        other.x = x
        other.y = y

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

    def go_right(self):
        self.right_flg = True
        self.move(0)

    def go_left(self):
        self.right_flg = False
        self.move(180)

    def go_random(self):
        rdm = random.randint(0, 10)
        if rdm < 5:
            self.go_right()
        else:
            self.go_left()

    def turn(self):
        self.right_flg = not self.right_flg
        if self.right_flg:
            self.go_right()
        else:
            self.go_left()

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

# Player
class PlayerSprite(BaseSprite):

    def __init__(self, x, y, u, v, spd):
        """ コンストラクタ """
        super().__init__(x, y, u, v, spd)

# Enemy
class EnemySprite(BaseSprite):

    def __init__(self, x, y, u, v, spd, player):
        """ コンストラクタ """
        super().__init__(x, y, u, v, spd)
        self.player = player # Player
        self.ijike_flg = False # Ijike
        self.ijike_cnt = 0
        self.ijike_limit = 72
        self.think_cnt = 0
        self.think_limit = 4

    def ijike_on(self):
        self.ijike_flg = True
        self.ijike_cnt = 0
        self.think_cnt = 0

    def ijike_off(self):
        self.ijike_flg = False
        self.ijike_cnt = 0
        self.think_cnt = 0

    def is_ijike(self):
        return self.ijike_flg

    def speed_up(self, accel):
        self.spd += accel

    def update(self):
        super().update()

        # Ijike Counter
        if self.ijike_flg:
            self.ijike_cnt += 1
            if self.ijike_limit < self.ijike_cnt:
                self.ijike_off()

        # Think Counter
        self.think_cnt += 1
        if self.think_limit < self.think_cnt:
            self.think_cnt = 0
            def_x = self.player.x - self.x
            if def_x < 0:
                if self.ijike_flg:
                    self.go_right()
                else:
                    self.go_left()
            else:
                if self.ijike_flg:
                    self.go_left()
                else:
                    self.go_right()

    def draw(self):
        # Animation
        self.u_anim_cnt += 1
        if self.u_anim_max < self.u_anim_cnt: self.u_anim_cnt = 0
        u = self.u_anim_cnt * 8
        v = 0 if self.right_flg else 8
        v += 16 if self.ijike_flg else 0 # Ijike
        pyxel.blt(self.x, self.y, 0, 
            self.u + u, self.v + v, self.w, self.h, 0)
        # Ijike
        if self.ijike_flg:
            ijike_remain = (self.ijike_limit - self.ijike_cnt) * 0.1
            str_ijike = "{}".format(math.floor(ijike_remain))
            x, _ = self.get_center()
            x -= (len(str_ijike) * 3) / 2
            pyxel.text(x, self.y-self.h, str_ijike, 7)

# Dot
class DotSprite(BaseSprite):

    def __init__(self, x, y, u, v, power_flg=False):
        """ コンストラクタ """
        super().__init__(x, y, u, v, 0)
        if power_flg: self.v += 8 # Power
        self.sleep_flg = False # Sleep or Awake
        self.power_flg = power_flg # Power or Normal

    def is_power(self):
        return self.power_flg

    def is_sleep(self):
        return self.sleep_flg

    def sleep(self):
        self.sleep_flg = True

    def awake(self):
        self.sleep_flg = False

    def draw(self):
        if self.sleep_flg == True: return
        super().draw()
