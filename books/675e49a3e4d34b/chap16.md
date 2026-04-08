---
title: "第16章(番外編): 吸血鬼射撃ゲーム(サンプル)"
---

# 吸血鬼射撃ゲーム(サンプル)

今回は、迫り来る怪物から逃げる感じのゲームを紹介します。
(ここでは、サンプルコードのみの紹介です)

## 1, 素材を用意する

"Pyxel Editor"で、背景の素材を描きます。
[リソースファイルをダウンロード](https://github.com/sdkfz181tiger/Zenn/blob/main/images/675e49a3e4d34b/vampire.pyxres) (右上の"ダウンロード"ボタンを押してダウンロードしてください)

![](/images/books/675e49a3e4d34b/16_01.png)

# サンプルコード

今回のサンプルコードは、次の通りです。

:::details 完成コード
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
        self.shot_interval = 12
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

    def __init__(self, x, y, u, v, spd, think_interval, target):
        """ コンストラクタ """
        super().__init__(x, y, u, v, spd)
        self.think_interval = think_interval
        self.think_counter = 0
        self.target = target

    def update(self):
        """ 更新処理 """
        super().update()
        # Think
        self.think_counter += 1
        if self.think_interval < self.think_counter:
            self.think_counter = 0
            direction = self.get_direction(self.target)
            self.move(direction)

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
        pyxel.rect(self.x, self.y, 2, 2, 7)

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
        pyxel.circ(self.x + self.off_x, self.y + self.off_y, self.circ_r, 7)

    def is_dead(self):
        """ 死亡フラグ """
        return self.life < 0
```

```python: main.py
import pyxel
import math
import random
import sprite

W, H = 160, 120

START_X = W / 2
START_Y = H / 2 - 10

MODE_TITLE = "title"
MODE_PLAY = "play"
MODE_GAME_OVER = "game_over"

PLAYER_SPD = 1.2
BULLET_SPD = 2.4

MONSTER_MAX = 10
MONSTERS = [
    {"u": 32, "v": 72, "spd": 0.1,  "think_interval": 60},
    {"u": 48, "v": 72, "spd": 0.12, "think_interval": 90},
    {"u":  0, "v": 80, "spd": 0.14, "think_interval": 120},
    {"u": 16, "v": 80, "spd": 0.16, "think_interval": 150},
    {"u": 32, "v": 80, "spd": 0.25, "think_interval": 180}
]

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # スコアを初期化
        self.score = 0

        # ゲームモード
        self.game_mode = MODE_TITLE

        # プレイヤーを初期化
        self.player = sprite.PlayerSprite(
            START_X, START_Y, 0, 72, PLAYER_SPD, self)

        # ステージを初期化
        self.reset()

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("vampire.pyxres")
        pyxel.run(self.update, self.draw) # Pyxel実行

    def update(self):
        """ 更新処理 """

        # コントロール
        self.control()

        # プレイ中判定
        if self.game_mode != MODE_PLAY: return

        # プレイヤーを更新
        self.player.update()
        self.overlap_area(self.player)

        # モンスター
        for monster in self.monsters[::-1]:
            monster.update()
            self.overlap_area(monster)
            # x プレイヤー
            if self.player.contains_center(monster):
                self.player.stop() # Stop
                self.game_mode = MODE_GAME_OVER
                pyxel.play(0, 16, loop=False) # サウンド

        # 弾丸
        for bullet in self.bullets[::-1]:
            bullet.update()
            if bullet.is_dead():
                self.bullets.remove(bullet) # Remove
            else:
                for monster in self.monsters[::-1]:
                    if monster.intersects(bullet):
                        self.bullets.remove(bullet) # Remove
                        self.append_particle(monster) # Particle
                        self.kick_area(monster) # Kick
                        self.score += 10 # Score
                        break

        # パーティクル
        for particle in self.particles[::-1]:
            particle.update()
            if particle.is_dead():
                self.particles.remove(particle) # Remove

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # タイルマップ
        pyxel.bltm(0, 0, 0, 0, 128, 192, 128, 0)

        # プレイヤーを描画
        self.player.draw()

        # モンスターを描画
        for monster in self.monsters:
            monster.draw()

        # 弾丸
        for bullet in self.bullets:
            bullet.draw()

        # パーティクル
        for particle in self.particles:
            particle.draw()

        # メッセージ
        if self.game_mode == MODE_TITLE:
            msg = "SPACE TO PLAY"
            pyxel.text(W/2-len(msg)*2, H/2, msg, 7)
            msg = "CONTROL: WASD"
            pyxel.text(W/2-len(msg)*2, H/2+10, msg, 7)
        elif self.game_mode == MODE_GAME_OVER:
            msg = "GAME OVER"
            pyxel.text(W/2-len(msg)*2, H/2, msg, 7)

        # スコアを描画
        pyxel.text(10, 10, 
            "SCORE:{:04}".format(self.score), 7)

    def reset(self):
        """ ステージを初期化 """

        # プレイヤー
        self.player.x = START_X
        self.player.y = START_Y

        # モンスター
        self.monsters = []
        for i in range(64):
            x = random.randint(0, W)
            y = random.randint(0, H)
            item = random.choice(MONSTERS)
            u = item["u"]
            v = item["v"]
            spd = item["spd"]
            think_interval = item["think_interval"]
            monster = sprite.Monster(x, y, u, v, spd, think_interval, self.player)
            # 距離を計算する
            distance = monster.get_distance(self.player)
            if distance < 24: continue
            # プレイヤーへの方向を計算する
            direction = monster.get_direction(self.player)
            monster.move(direction)
            self.monsters.append(monster)

        # 弾丸
        self.bullets = []
        # パーティクル
        self.particles = []

    def control(self):
        """ コントロール """

        # ゲームループ
        if pyxel.btnp(pyxel.KEY_SPACE):

            # Title -> Play
            if self.game_mode == MODE_TITLE:
                self.game_mode = MODE_PLAY

            # Game Over -> Title
            if self.game_mode == MODE_GAME_OVER:
                self.game_mode = MODE_TITLE
                # Reset
                self.reset()

            return

        # プレイヤー
        if self.game_mode == MODE_PLAY:

            # W
            if pyxel.btnp(pyxel.KEY_W):
                self.player.move(270)
            elif pyxel.btnr(pyxel.KEY_W):
                self.player.stop()
            # A
            if pyxel.btnp(pyxel.KEY_A):
                self.player.move(180)
            elif pyxel.btnr(pyxel.KEY_A):
                self.player.stop()
            # S
            if pyxel.btnp(pyxel.KEY_S):
                self.player.move(90)
            elif pyxel.btnr(pyxel.KEY_S):
                self.player.stop()
            # D
            if pyxel.btnp(pyxel.KEY_D):
                self.player.move(0)
            elif pyxel.btnr(pyxel.KEY_D):
                self.player.stop()

    def overlap_area(self, spr):
        """ オーバーラップ """
        if W < spr.x: spr.x = 0
        if spr.x < 0: spr.x = W
        if H < spr.y: spr.y = 0
        if spr.y < 0: spr.y = H

    def kick_area(self, spr):
        """ 画面端に強制移動 """
        num = random.randint(0, 2)
        if num == 0:
            y = random.randint(0, H)
            spr.set_center(0, y) # Horizontal
        else:
            x = random.randint(0, W)
            spr.set_center(x, 0) # Vertical
        pyxel.play(1, 1, loop=False) # サウンド

    def get_nearest_monster(self):
        """ 最も近いモンスターの座標 """
        distance_min = 999
        nearest = None
        for monster in self.monsters:
            distance = monster.get_distance(self.player)
            if distance_min < distance: continue
            distance_min = distance # Nearest
            nearest = monster
        return nearest

    def on_shot_event(self, spr):
        """ 弾丸発射 """
        # 弾丸
        if not self.monsters: return
        x, y = spr.get_center()
        bullet = sprite.Bullet(x, y, BULLET_SPD)
        monster = self.get_nearest_monster()
        direction = self.player.get_direction(monster)
        bullet.move(direction)
        self.bullets.append(bullet)
        #pyxel.play(1, 0, loop=False) # サウンド

    def append_particle(self, spr):
        """ パーティクル発生 """
        x, y = spr.get_center()
        particle = sprite.Particle(x, y)
        self.particles.append(particle)

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()
```
:::

実行結果は次のようになります。

![](/images/books/675e49a3e4d34b/16_02.gif)

# 終わりに...

ここまで読んでいただきありがとうございました。
この連載が、ゲーム開発のきっかけになれば幸いです。ޱ(ఠ皿ఠ)ว
(よろしければ👍頂けると大変励みになります!!)