---
title: "第17章(番外編): パクパク追いかけゲーム(サンプル)"
---

# パクパク追いかけゲーム(サンプル)

今回は、ドットを食べつつ、追いかけっこをするゲームを紹介します。
(ここでは、サンプルコードのみの紹介です)

## 1, 素材を用意する

"Pyxel Editor"で、背景の素材を描きます。
[リソースファイルをダウンロード](https://github.com/sdkfz181tiger/Zenn/blob/main/images/675e49a3e4d34b/pacman.pyxres) (右上の"ダウンロード"ボタンを押してダウンロードしてください)

![](/images/books/675e49a3e4d34b/17_01.png)

# サンプルコード

今回のサンプルコードは、次の通りです。

:::details 完成コード(sprite.py)
```python: sprite.py
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

```
:::

:::details 完成コード(main.py)
```python: main.py
# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random
import sprite

W, H = 160, 120

MODE_GAME_READY = "mode_game_ready"
MODE_GAME_PLAY = "mode_game_play"
MODE_GAME_OVER = "mode_game_over"

TOTAL_DOTS = 12
SCORE_DOT = 10
SCORE_IJIKE = 40

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # Player
        self.player = sprite.PlayerSprite(
            0, 0, 0, 8, 1.8)

        # Enemy
        self.enemy = sprite.EnemySprite(
            0, 0, 0, 40, 0.8, self.player)

        # Dots
        self.dots = []
        # ステップ2: ドットを配置
        pad_x = W / TOTAL_DOTS
        for i in range(TOTAL_DOTS):
            x = i * pad_x + pad_x / 2
            self.create_dot(x, H/2, i==0)

        # Ready
        self.game_ready()

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("pacman.pyxres")
        pyxel.run(self.update, self.draw) # Pyxel実行

    def update(self):
        """ 更新処理 """

        self.control() # Control
        if self.mode != MODE_GAME_PLAY: return

        # Player
        self.player.update()
        self.overlap_area(self.player) # Overlap

        # Enemy
        self.enemy.update()
        self.overlap_area(self.enemy) # Overlap

        # Dots
        for dot in self.dots:
            dot.update()
            # Contains and Sleep
            if dot.is_sleep(): continue
            if self.player.contains_center(dot):
                self.score += SCORE_DOT # Score
                dot.sleep()
                if dot.is_power():
                    self.enemy.ijike_on() # Ijike(On)

        # Awake all dots
        if self.is_sleep_dots():
            self.awake_dots()
            self.level_up() # Level Up!!

        # Collision
        if self.player.contains_center(self.enemy):
            if self.enemy.is_ijike():
                self.score += SCORE_IJIKE # Score
                self.enemy.set_center(0, H/2) # Reset
                self.enemy.ijike_off() # Ijike(Off)
            else:
                # ステップ4: ゲームオーバー判定
                self.game_over() # Game Over
            
    def draw(self):
        """ 描画処理 """
        pyxel.cls(1)

        # Road
        pyxel.rect(0, H/2-8, W, 16, 0)
        pyxel.rect(0, H/2-9, W, 1, 5)
        pyxel.rect(0, H/2+8, W, 1, 5)

        # Dots
        for dot in self.dots:
            dot.draw()
        # Player
        self.player.draw()
        # ステップ3: 敵を描画
        # Enemy
        self.enemy.draw()
        # Stats
        self.draw_stats()

    def create_dot(self, x, y, power_flg):
        dot = sprite.DotSprite(0, 0, 0, 16, power_flg)
        dot.set_center(x, y)
        self.dots.append(dot)

    def overlap_area(self, spr):
        # ステップ1: オーバーラップ処理
        if spr.x < 0: spr.x = W
        if W < spr.x: spr.x = 0

    def draw_stats(self):
        # Level
        str_level = "LV:{}".format(self.level)
        x = W - (len(str_level) * 4) - 10
        pyxel.text(x, 10, str_level, 7)
        # Score
        str_score = "SCORE:{:03}".format(self.score)
        x = 10
        pyxel.text(x, 10, str_score, 7)
        # Message
        str_msg = "{}".format(self.msg)
        x = W / 2 - (len(str_msg) * 4) / 2
        pyxel.text(x, H/2 - 24, str_msg, 7)

    def control(self):
        """ コントロール """
        if not pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT): return

        # Ready to Play
        if self.mode == MODE_GAME_READY:
            self.game_play() # Play
            return

        # Play
        if self.mode == MODE_GAME_PLAY:
            self.player.turn() # Turn
            return

        # Over to Ready
        if self.mode == MODE_GAME_OVER:
            self.game_ready() # Ready
            return

    def game_ready(self):
        self.mode = MODE_GAME_READY
        self.msg = "GAME READY!?"
        self.level = 1 # Level
        self.score = 0 # Score
        self.player.set_center(W/2, H/2) # Player
        self.enemy.set_center(0, H/2) # Enemy
        self.awake_dots() # Awake

    def game_play(self):
        self.mode = MODE_GAME_PLAY
        self.msg = "GAME PLAY!!"
        self.player.go_random() # Player
        self.enemy.go_random() # Enemy

    def game_over(self):
        self.mode = MODE_GAME_OVER
        self.msg = "GAME OVER!!"
        self.player.stop() # Player
        self.enemy.stop() # Enemy

    def is_sleep_dots(self):
        if not self.dots: return False
        for dot in self.dots:
            if not dot.is_sleep(): return False
        return True

    def awake_dots(self):
        # Awake
        for dot in self.dots:
            dot.awake()
        # Swap
        if 0 < len(self.dots):
            other = random.choice(self.dots)
            self.dots[0].swap_position(other)

    def level_up(self):
        self.level += 1 # Level Up!!
        self.enemy.speed_up(0.14) # Speed Up!!

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()
```
:::

実行結果は次のようになります。

![](/images/books/675e49a3e4d34b/17_02.gif)

# 終わりに...

ここまで読んでいただきありがとうございました。
この連載が、ゲーム開発のきっかけになれば幸いです。ޱ(ఠ皿ఠ)ว
(よろしければ👍頂けると大変励みになります!!)